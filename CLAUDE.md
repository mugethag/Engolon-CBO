# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Engolon CBO is a Kenya-based community organization website with two distinct components:

1. **Main Website** (`index.html`, `assets/`) — Static HTML/CSS/JS site, no build step required
2. **Robotics Certificate Course** (`robotics-cbi-orientation/`) — HyperFrames video composition project with a parallel pilot LMS site

## Main Website

**No build process.** Open `index.html` directly in a browser, or use any static file server.

Files to edit:
- `index.html` — content and structure
- `assets/css/styles.css` — styling and responsive breakpoints
- `assets/js/script.js` — interactive features (hamburger menu, counters, form validation, modals)
- `assets/js/course-auth.js` — SHA-256 browser-side password gate for the robotics course

**Color palette** (used across both components):
- Primary Green: `#2D5016`
- Primary Orange: `#C97A4A`
- Cream background: `#f5f1eb`
- Dark text: `#333333`

**Responsive breakpoints**: Mobile < 768px (hamburger menu, single-column), Tablet 768–1023px (2-col), Desktop 1024px+ (4-col, full nav).

## Course Authentication

`robotics-certificate.html` uses a browser-side SHA-256 password hash stored in `assets/js/course-auth.js`. Access state persists via `localStorage`. This is a temporary gate — Moodle LMS integration is planned. See `COURSE_ACCESS.md` for how to update the password hash.

## Robotics Course (HyperFrames)

The `robotics-cbi-orientation/` directory is a HyperFrames composition project. **Read `robotics-cbi-orientation/CLAUDE.md` before editing any composition HTML** — it documents required data attributes, `window.__timelines` registration, and linting rules that are mandatory.

```bash
cd robotics-cbi-orientation
npm run dev      # preview in browser
npm run check    # lint + validate (always run after changes)
npm run render   # export to MP4
npm run publish  # publish and get shareable link
```

HyperFrames design system: dark editorial theme with Cyan `#55c7d9` and Green `#00aa6c` accents. See `robotics-cbi-orientation/DESIGN.md` for motion and visual identity guidelines.

## Course Content Production

- Module scripts, storyboards, quizzes, and handouts live in `robotics-cbi-orientation/course-mvp/term-1/module-*/`
- Modules 1 & 2 serve as production templates for new modules
- `COURSE_PRODUCTION_TRACKER.md` tracks the full 12-module roadmap and Moodle setup checklist
- The pilot LMS site (`robotics-cbi-orientation/pilot-site/`) is a standalone HTML prototype with `index.html`, `admin.html`, `portal.html`, and `project-brief.html`

## Deployment

The main site is deployed via **Netlify** (`.netlify/state.json` present). GitHub remote: `https://github.com/mugethag/Engolon-CBO.git`.

## Agent skills

### Issue tracker

Issues live in GitHub Issues (`github.com/mugethag/Engolon-CBO`). See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-role vocabulary — no custom overrides. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context — one `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
