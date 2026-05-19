# Engolon CBO — Automated Social Media Marketing System
**Date:** 2026-05-19  
**Status:** Approved for implementation  
**Phase:** 1 of 2 (text/photo content pipeline; video pipeline deferred)

---

## Goal

Grow Engolon CBO's social media presence on Facebook, Instagram, YouTube, and X/Twitter to drive **donor acquisition and fundraising**. Achieve this through a daily automated pipeline that monitors the Kenya/Africa impact-creator space, detects high-performing content patterns, and generates original, on-brand posts adapted to Engolon's voice.

---

## Scope

### In scope (Phase 1)
- Brand voice profile builder
- NGO/impact creator monitoring (YouTube + X/Twitter)
- Outlier detection and pattern analysis
- Caption, hook, and carousel script generation via Claude API
- Google Sheets dashboard (7 tabs)
- Daily Gmail digest to mugethag@gmail.com
- GitHub Actions scheduling (free cloud runner)

### Deferred to Phase 2
- Video Editing Agent (Descript API) — requires active video production workflow
- Thumbnail Agent (Nana Banana Pro) — requires video content
- Instagram/Facebook posting automation — Phase 1 generates drafts; posting is manual

---

## Architecture

### Project structure

```
Engolon CBO/
└── social-media/
    ├── agents/
    │   ├── brand_agent.py        # Engolon voice profile builder
    │   ├── research_agent.py     # NGO/impact creator monitoring
    │   ├── trend_agent.py        # Outlier detection
    │   ├── script_agent.py       # Caption/post/carousel generation
    │   └── digest_agent.py       # Sheets → Gmail daily email
    ├── integrations/
    │   ├── sheets.py             # Google Sheets read/write helpers
    │   ├── gmail.py              # Gmail send helpers
    │   ├── youtube.py            # YouTube Data API wrapper
    │   └── claude_client.py      # Anthropic SDK wrapper
    ├── data/
    │   └── brand_profile.json    # Local cache (committed to repo by weekly workflow)
    ├── utils/
    │   ├── logger.py
    │   └── retry.py
    ├── .env.example
    ├── requirements.txt
    └── README.md
```

### Data flow

```
[brand_agent] ──writes──> brand_profile.json
                                │
           ┌────────────────────┘
           ▼
[research_agent] ──writes──> Competitor Tracking tab
           │
           ▼
[trend_agent] ──reads Competitor Tracking──> Trend Outliers tab
           │
           ▼
[script_agent] ──reads top 3 outliers + brand_profile──> Scripts tab
           │
           ▼
[digest_agent] ──reads all tabs (last 24h)──> Gmail to mugethag@gmail.com
```

---

## Agent Definitions

### `brand_agent`
**Trigger:** Manual (setup) + weekly cron (Sunday)  
**Input:** `index.html`, mission docs, program descriptions from website  
**Process:** Sends Engolon content to Claude API; extracts mission, tone, target audience, content pillars (women, children, elderly, PWDs), fundraising language style, hook patterns  
**Output:** Writes to both **Brand Voice Profile** tab in Google Sheets (primary, always available to all agents) and commits `data/brand_profile.json` to the repo as a human-readable reference. Other agents always read from Sheets, not the local file, since GitHub Actions runners are ephemeral.

### `research_agent`
**Trigger:** Daily cron (06:00 EAT)  
**Input:** Competitor/monitor list from Config tab in Google Sheets  
**Process:** Fetches recent posts/videos via YouTube Data API (primary source). For X/Twitter: uses X API v2 Basic tier ($100/month) if available; if not configured, gracefully skips X and logs a notice in the digest. Extracts topic, format, engagement metrics, creator size.  
**Output:** Rows appended to **Competitor Tracking** tab

### `trend_agent`
**Trigger:** Daily, after `research_agent`  
**Input:** Competitor Tracking tab  
**Process:**
- Calculates `outlier_score = recent_engagement / creator_30day_avg_engagement`
- Flags score ≥ 2.5× (or ≥ 1.8× for creators < 10k followers)
- Sends outlier to Claude API to extract: hook pattern, emotional trigger, why it worked, adaptation idea for Engolon  
**Output:** Rows appended to **Trend Outliers** tab

### `script_agent`
**Trigger:** Daily, after `trend_agent`  
**Input:** Top 3 outliers from Trend Outliers tab + `brand_profile.json`  
**Process:** For each outlier, calls Claude API to generate:
- Caption for Facebook/Instagram (donor-acquisition angle)
- Hook line (≤ 10 words)
- 3 talking points
- CTA (donate link, volunteer sign-up, or share)
- Optional carousel slide outline  
**Adaptation rule in system prompt:** *"Do not copy this content. Identify the emotional trigger and format pattern. Generate an original post for Engolon CBO that serves our donor acquisition goal."*  
**Output:** Rows appended to **Content Ideas** and **Scripts** tabs

### `digest_agent`
**Trigger:** Daily, after `script_agent`  
**Input:** All sheet tabs (last 24h rows); error log from upstream agents  
**Process:** Composes prioritized HTML email: top outliers, best adaptation ideas, 3 scripts ready to use, any errors  
**Output:** Gmail sent to mugethag@gmail.com

---

## Google Sheets Schema

**Spreadsheet:** One workbook, seven tabs

| Tab | Key Columns |
|---|---|
| Brand Voice Profile | Version, Date, Mission, Tone, Audience, Content Pillars, Fundraising Style, Hook Patterns |
| Competitor Tracking | Date, Platform, Creator, Subscriber Count, Post URL, Topic, Format, Views/Likes, Creator Avg, Outlier Score |
| Trend Outliers | Date, Creator, URL, Topic, Hook Pattern, Why It Works, Emotional Trigger, Adaptation Idea, Status |
| Content Ideas | Date, Source Outlier, Platform, Hook, Concept Summary, Format, Fundraising Angle, Priority (1–3) |
| Scripts | Date, Platform, Hook, Caption, Talking Points, CTA, Carousel Outline, Status (Draft/Approved/Posted) |
| Daily Digest Archive | Date, Email Subject, Outliers Found, Scripts Generated, Errors |
| Config | Competitor channel list, outlier threshold, digest recipient email |

The **Config tab** is the operator panel — add/remove competitors and adjust thresholds without touching code.

---

## GitHub Actions Scheduling

**Three workflow files** in `.github/workflows/`:

| File | Trigger | Purpose |
|---|---|---|
| `social-media-setup.yml` | Manual (`workflow_dispatch`) | Runs `brand_agent` once on setup |
| `social-media-daily.yml` | Cron `0 3 * * *` (06:00 EAT) | Full daily pipeline |
| `social-media-weekly.yml` | Cron `0 2 * * 0` (05:00 EAT Sunday) | Refreshes brand profile — runs 1 hour before daily pipeline on Sundays |

**Daily job order** (sequential; `digest_agent` always runs even if upstream fails):
```
research_agent → trend_agent → script_agent → digest_agent
```

**GitHub Actions secrets required:**
```
ANTHROPIC_API_KEY
GOOGLE_CREDENTIALS_JSON    # Service account JSON, base64-encoded
YOUTUBE_API_KEY
GMAIL_RECIPIENT            # mugethag@gmail.com
SPREADSHEET_ID
```

---

## Competitor Seed List (Config tab, initial values)

| Category | Accounts |
|---|---|
| Kenya NGOs/CBOs | Kenya Red Cross, SHOFCO, Kidogo, Amref Health Africa |
| East Africa impact | UNICEF Kenya, UN Women Africa, Ashoka East Africa |
| Fundraising inspiration | GlobalGiving, GoFundMe Stories |

Fully editable in the Config tab — no code change needed to add/remove.

---

## Error Handling

- Each agent wraps API calls in retry logic (3 attempts, exponential backoff)
- Agent failures are caught, logged to `utils/logger.py`, and passed to `digest_agent`
- `digest_agent` always runs — errors appear in the daily email so nothing fails silently
- Rate limit errors pause and retry after cooldown; if unresolvable, skip and log

---

## Phase 2 (Future)

When Engolon has a consistent video production workflow:
- **Video Editing Agent** — Descript API integration for auto-editing phone-shot footage
- **Thumbnail Agent** — Nana Banana Pro for YouTube thumbnail generation
- **Publishing Agent** — Auto-post approved scripts to Facebook/Instagram via their APIs
