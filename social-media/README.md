# Engolon CBO Social Media Automation System

Automated daily pipeline that monitors Kenya/Africa NGO content, detects outlier patterns, generates original donor-acquisition posts, and delivers a daily digest email. Runs free on GitHub Actions.

## Architecture

Five sequential agents, each writing to Google Sheets tabs that the next agent reads:

```
brand_agent → Brand Voice Profile tab
research_agent → Competitor Tracking tab
trend_agent → Trend Outliers tab
script_agent → Scripts + Content Ideas tabs
digest_agent → Daily Digest Archive tab + Gmail
```

## One-Time Setup

### 1. Google Cloud

1. Create a project at [console.cloud.google.com](https://console.cloud.google.com)
2. Enable: **Google Sheets API**, **YouTube Data API v3**
3. Create a Service Account → download JSON key
4. Create a Google Sheet → share it with the service account email as **Editor**
5. Copy the Spreadsheet ID from the URL (between `/d/` and `/edit`)

### 2. API Keys

| Key | Where to get it |
|---|---|
| `OPENAI_API_KEY` | [platform.openai.com](https://platform.openai.com) -> API keys |
| `OPENAI_MODEL` | Optional. Defaults to `gpt-4.1-mini` if unset |
| `YOUTUBE_API_KEY` | Google Cloud → APIs & Services → Credentials → API Key |
| `GMAIL_APP_PASSWORD` | Gmail → Google Account → Security → App Passwords |

### 3. GitHub Actions Secrets

Go to your repo → Settings → Secrets and variables → Actions. Add:

| Secret | Value |
|---|---|
| `OPENAI_API_KEY` | OpenAI API key |
| `OPENAI_MODEL` | Optional model override, e.g. `gpt-4.1-mini` |
| `GOOGLE_CREDENTIALS_JSON` | Base64-encoded service account JSON: `base64 -w0 service-account.json` |
| `YOUTUBE_API_KEY` | YouTube API key |
| `GMAIL_SENDER` | `mugethag@gmail.com` |
| `GMAIL_RECIPIENT` | `mugethag@gmail.com` |
| `GMAIL_APP_PASSWORD` | 16-char Gmail App Password |
| `SPREADSHEET_ID` | Google Sheets ID from the URL |

### 4. Create Spreadsheet Tabs

Copy `.env.example` to `.env`, fill in real values, then run:

```bash
cd social-media
pip install -r requirements.txt
python scripts/setup_sheets.py
```

This creates 7 tabs with headers and seeds the Config tab with competitor channel placeholders.

### 5. Update Config Tab

Open the Google Sheet → Config tab. Replace every `REPLACE_WITH_CHANNEL_ID` with a real YouTube channel ID. Find channel IDs by visiting `youtube.com/@ChannelName/about` and viewing the page source.

### 6. Run Initial Brand Setup

In GitHub → Actions → "Social Media — Setup (Brand Agent)" → Run workflow.

This analyzes `index.html` and writes the brand voice profile to the Brand Voice Profile tab.

## Daily Operation

The pipeline runs automatically at **06:00 EAT** every day via the `social-media-daily.yml` workflow. You receive an email digest each morning.

To trigger manually: GitHub → Actions → "Social Media — Daily Pipeline" → Run workflow.

## Local Development

```bash
cd social-media
cp .env.example .env    # fill in real values
pip install -r requirements.txt

python -m agents.brand_agent       # build brand profile
python -m agents.research_agent    # fetch competitor videos
python -m agents.trend_agent       # detect outliers
python -m agents.script_agent      # generate posts
python -m agents.digest_agent      # send email
```

## Tests

```bash
cd social-media
pytest tests/ -v
```

Expected: 17 tests, all passing.

## Google Sheets Dashboard

| Tab | Purpose |
|---|---|
| Brand Voice Profile | Engolon's voice/mission extracted by brand_agent |
| Competitor Tracking | Recent videos from monitored channels |
| Trend Outliers | Content significantly outperforming creator averages |
| Content Ideas | Post concepts for each outlier |
| Scripts | Full captions, hooks, CTAs ready to copy |
| Daily Digest Archive | History of every digest email sent |
| Config | Edit competitor channel list here (no code change needed) |
