---
name: Engolon CBO
description: Dark editorial identity for a Kenya-based community organization — archive black, warm serif typography, and a single flame-orange accent.
colors:
  community-flame: "#e8833a"
  community-flame-deep: "#d4722a"
  archive-black: "#0d0d0d"
  deep-black: "#080808"
  surface-alt: "#111111"
  card-surface: "#1a1a1a"
  card-surface-alt: "#161616"
  warm-white: "#f5f0e8"
typography:
  display:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: "clamp(3rem, 5vw, 6rem)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: "3rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  title:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: "2.25rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  body:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: "normal"
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: "0.7rem"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "0.14em"
rounded:
  sm: "4px"
  lg: "6px"
  pill: "100px"
spacing:
  1: "0.5rem"
  2: "1rem"
  3: "1.5rem"
  4: "2rem"
  6: "3rem"
  8: "4rem"
  12: "6rem"
components:
  button-primary:
    backgroundColor: "{colors.community-flame}"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
    padding: "0.75rem 1.75rem"
  button-primary-hover:
    backgroundColor: "{colors.community-flame-deep}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.warm-white}"
    rounded: "{rounded.sm}"
    padding: "0.75rem 1.75rem"
  program-card:
    backgroundColor: "{colors.card-surface}"
    rounded: "0"
    padding: "{spacing.4}"
  testimonial-card:
    backgroundColor: "{colors.card-surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.5}"
---

# Design System: Engolon CBO

## 1. Overview

**Creative North Star: "The Community Archive"**

This system is built as a living record: dark and permanent like newsprint archive or documentary film, warm and specific in its accents like the orange glow of a community cooking fire. The canvas is near-total dark (#0d0d0d) — not atmospheric, not decorative — because it makes every image, every word, every orange accent feel like evidence. Things preserved. Things that matter.

Playfair Display carries the editorial gravity: the italic `em.accent` pattern inside headings is the system's most distinctive voice move — a phrase breaking into warmth mid-sentence, as if the speaker is leaning in. Lora handles body prose: unhurried, literate, designed for long reading. System sans handles UI metadata (labels, tags, captions): legible, invisible, stepping aside for the serifs.

The single accent — Community Flame (#e8833a) — earns its place through rarity and specificity. It appears on CTAs, hover states, active borders, section labels, and the marquee strip. Nowhere else. Its warmth against the dark ground is the entire emotional charge of the system.

This system explicitly rejects: the blue-and-stock-photo charity aesthetic of large international aid organizations; poverty-framing imagery or guilt-tone copy; the polished-but-soulless corporate nonprofit look. It also rejects the editorial-magazine lane (drop caps, broadsheet grids, italic Cormorant everywhere) that has become AI scaffolding.

**Key Characteristics:**
- Near-total dark canvas with a single warm-orange accent
- Serif-on-serif typography with system sans for UI metadata
- Orange italic emphasis pattern inside headings (the `em.accent` convention)
- Documentary imagery approach: real faces, real places, real situations
- Cards and containers are flat at rest; depth reveals on interaction

## 2. Colors: The Archive Palette

One accent color against a spectrum of near-blacks. The system's entire warmth lives in the orange; the darks provide its weight.

### Primary
- **Community Flame** (`#e8833a`): The singular warm accent. CTAs, section labels, hover color for nav links and headings, card top-border accents, the orange-bg marquee strip. The warmth that earns its place through restriction.
- **Community Flame Deep** (`#d4722a`): Hover and pressed state for Community Flame. Slightly deeper and more saturated — the fire pulling inward.

### Neutral
- **Archive Black** (`#0d0d0d`): Body background. Near-total dark but not `#000000` — the very slight lift creates room for deeper tones to register.
- **Deep Black** (`#080808`): Footer background only. Deeper than the body, providing spatial closure at the bottom of each page.
- **Surface Alt** (`#111111`): Alternate section background (`.section-alt`). One tone lighter than Archive Black — just enough to signal a new section without breaking the dark world.
- **Card Surface** (`#1a1a1a`): Cards, inline panels, containers. Clearly distinct from the page background, still deep.
- **Warm White** (`#f5f0e8`): Primary text. A slight amber lean, not pure white — warm against the dark ground, matching the orange accent's hue family. Contrast against Archive Black: approximately 17:1.
- **Muted Warm White** (`rgba(245, 240, 232, 0.60)`): Secondary text, body paragraphs, captions. Approximately 40% of Warm White's presence.
- **Border Subtle** (`rgba(245, 240, 232, 0.08)`): Structural dividers, card borders at rest. Near-invisible; structural but not assertive.
- **Border Mid** (`rgba(245, 240, 232, 0.15)`): Medium-state borders, hover borders on cards.

### Named Rules
**The One Flame Rule.** Community Flame is used in exactly one role at a time on any given screen. Navigation hover OR card top-accent OR section label OR CTA button. When everything is orange, nothing is. Reserve the accent for the moments that need to speak.

**The No Pure White Rule.** Never use `#ffffff` for body text. Warm White (#f5f0e8) is the ceiling. Pure white reads as blown-out against the dark ground; the slight warmth grounds the text in the same hue family as the accent.

## 3. Typography

**Display Font:** Playfair Display (italic available, weights 400 and 700), with Georgia and serif fallbacks  
**Body Font:** Lora (weight 400), with Georgia and serif fallbacks  
**Label Font:** System sans-serif (-apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue")

**Character:** Two serifs and a system sans. Playfair Display commands — architectural, editorial, italic-capable. Lora reads — warm, measured, built for paragraphs. The system sans steps aside — it carries labels, tags, and captions without competing. The pairing is role-based contrast, not style contrast.

### Hierarchy
- **Display** (weight 700, `clamp(3rem, 5vw, 6rem)`, line-height 1.05, letter-spacing -0.02em): Hero headlines only. The `em.accent` inside display headings adds italic orange warmth mid-phrase — the system's voice signature.
- **Headline** (weight 700, 3rem, line-height 1.2, letter-spacing -0.02em): Section h1 headings. Pairs with the section label pattern above.
- **Title** (weight 700, 2.25rem, line-height 1.2, letter-spacing -0.01em): Section h2 headings. Slightly pulled back from Headline in both size and spacing.
- **Subtitle** (weight 600, 1.375rem, line-height 1.2): h3 headings, card titles.
- **Body** (weight 400, 1rem, line-height 1.75, Lora): Main prose. Line-height 1.75 is deliberate on a dark background — light type needs more breathing room than dark-on-light. Maximum line length: 65–75ch.
- **Label** (weight 600–700, 0.68–0.8125rem, uppercase, letter-spacing 0.12–0.15em, system sans): Section eyebrows, program locations, stat labels, card tags. All-caps at this size only.

### Named Rules
**The Italic Accent Rule.** `em.accent` inside headings always renders in Community Flame, italic. This is the only sanctioned use of italic as a color carrier. Do not add it to body copy. One accent phrase per heading.

**The Sans Ceiling Rule.** System sans-serif is for UI metadata only: labels under 1rem, tags, captions, nav links, stat descriptions. Above 1rem, Lora or Playfair Display owns the voice. Mixing sans into body prose breaks the archival register.

## 4. Elevation

The system uses shadow-based depth with a dark-canvas calibration: shadows are very high opacity (0.3–0.6) because near-black backgrounds make standard 0.1–0.15 alpha shadows invisible. Surfaces are flat at rest; shadow appears as a response to state (hover, floating elements).

### Shadow Vocabulary
- **xs** (`0 1px 2px rgba(0, 0, 0, 0.3)`): Hairline lift. Used on fine-detail elements where structure needs to be suggested without distraction.
- **sm** (`0 2px 4px rgba(0, 0, 0, 0.4)`): Ambient card rest state. Testimonial cards, gallery images at rest.
- **md** (`0 4px 12px rgba(0, 0, 0, 0.5)`): Hover lift. Applied when cards or buttons elevate on hover — the primary interactive feedback.
- **lg** (`0 8px 24px rgba(0, 0, 0, 0.6)`): Modal and floating panels. Not used in main content flow.

### Named Rules
**The Dark Canvas Shadow Rule.** Never use the same shadow values from a light-bg project. Archive Black absorbs standard shadows. Minimum 0.3 alpha for xs; 0.4+ for ambient; 0.5+ for interactive states. If a shadow is invisible, it should be removed, not faked with a border.

## 5. Components

### Buttons

Confident and direct: no rounding beyond 4px, uppercase labels, strong orange on dark ground.

- **Shape:** Square-ish (4px radius). Not rounded; not pill. Signals authority.
- **Primary:** Community Flame background (#e8833a), white text (#ffffff), 12px 28px padding, uppercase, weight 700, 0.08em letter-spacing. Minimum width 160px.
- **Hover / Focus:** Community Flame Deep (#d4722a) background, translateY(-1px) lift, md shadow.
- **Outline:** Transparent background, Warm White text, 1px `rgba(245, 240, 232, 0.4)` border. Hover: border becomes fully opaque, very subtle warm-white background tint. No fill change.
- **Nav CTA (Donate):** Same as Primary but without minimum width; slightly smaller padding (10px 22px). Inline in the nav bar.

### Tags / Chips

- **Style:** `rgba(245, 240, 232, 0.06)` background, 100px radius (pill), 1px subtle border, muted warm-white text, 0.68rem sans-serif, 0.04em letter-spacing. No interaction state — purely informational.

### Program Cards

The primary content container. Warm but structured.

- **Corner Style:** Zero radius (sharp corners). The editorial ground doesn't soften its containers.
- **Background:** Card Surface (#1a1a1a).
- **Top accent:** 3px Community Flame top border — the orange announces each card from above.
- **Full border:** 1px Border Subtle wrapping the card.
- **Internal Padding:** 2rem (--space-4) on all sides.
- **Hover:** translateY(-3px) lift only. No shadow increase, no border color change — the lift is the signal.

### Testimonial Cards

- **Corner Style:** Gently curved (6px radius).
- **Background:** Card Surface (#1a1a1a).
- **Border:** 1px Border Subtle at rest; 1px Border Mid on hover.
- **Shadow:** sm at rest; md on hover.
- **Hover:** translateY(-4px) lift; orange top-border reveals.
- **Internal Padding:** 2.5rem (--space-5).

### Form Inputs

- **Style:** `rgba(245, 240, 232, 0.05)` background (barely there), 1px `rgba(245, 240, 232, 0.2)` border, 4px radius.
- **Text:** Warm White (#f5f0e8), 1rem, system sans.
- **Focus:** Border color shifts to Community Flame (#e8833a); 3px glow ring `rgba(232, 131, 58, 0.15)`. Background lifts slightly to 0.07 opacity.
- **Label:** 0.875rem, weight 600, Warm White, 0.04em tracking.

### Navigation

The system's orienting band. Dark and unobtrusive until hover.

- **Style:** Sticky, Archive Black (#0d0d0d) background, 1px Border Subtle bottom border.
- **Logo:** Playfair Display, 1.4rem, weight 700, uppercase, 0.15em letter-spacing. Logo image is circular (50% radius, 48px).
- **Links:** System sans, 0.75rem, weight 500, uppercase, 0.12em letter-spacing, Warm White at rest. Hover: Community Flame.
- **Mobile:** Hamburger at < 768px. Animated to X on open (rotation + cross transform).

### Marquee Strip

A signature component: full-width Community Flame band between hero and content.

- **Background:** Community Flame (#e8833a).
- **Content:** White uppercase text, 0.75rem, weight 600, 0.1em letter-spacing. Continuous left-scroll at 30s duration.
- **Purpose:** Announces programs as a living ticker. Provides a full-bleed orange break between hero and content — the visual moment when the accent "breathes."

### Stats Bar

Three-column centered stats on Surface Alt (#111111), separated by 1px Border Subtle vertical dividers.

- **Numbers:** Playfair Display, 3rem, weight 700, Warm White.
- **Labels:** System sans, 0.7rem, uppercase, 0.15em letter-spacing, Muted Warm White.

## 6. Do's and Don'ts

### Do:
- **Do** use Community Flame sparingly: one active role per screen at a time. Its rarity is the signal.
- **Do** use the `em.accent` italic pattern inside headings for key phrases. This is the system's voice signature — orange italic within a Playfair Display heading.
- **Do** calibrate shadows for the dark canvas: minimum 0.3 alpha on xs; the archive-black ground absorbs standard 0.1 shadows into invisibility.
- **Do** use real community imagery: specific people, specific places, specific moments. Kibra, Kajiado, Nairobi are real places; design should feel situated in them.
- **Do** let Warm White (#f5f0e8) be the text ceiling. No pure white (#ffffff) in body copy.
- **Do** match the section-label pattern (small uppercase orange sans, before h2) to named sections, used deliberately — not as reflexive scaffolding on every heading.
- **Do** write alt text in the brand voice: "Women in tailoring training, Kibra community" over "women sewing".

### Don't:
- **Don't** use the generic NGO charity aesthetic: blue-and-stock-photo, "helping hands" imagery, or the UNICEF/Red Cross visual register. This organization is local-first; it should feel situated in Nairobi, not headquartered elsewhere.
- **Don't** use poverty-framing or guilt-tone copy. The brand voice celebrates community agency. Every image and sentence should affirm the humanity and capability of the people shown, not exploit their difficulty.
- **Don't** use the corporate nonprofit look: polished, consistent, cold. If a page could belong to a Fortune 500 CSR report, it's wrong for this brand.
- **Don't** add gradient text (`background-clip: text` with a gradient). Use solid Community Flame for emphasis, or increase font weight.
- **Don't** use glassmorphism decoratively. Blur and backdrop-filter are not this system's materials.
- **Don't** repeat the section eyebrow (`section-label`) on every heading as reflex scaffolding. Use it where it carries specific named information; omit it where it would just say "SECTION".
- **Don't** use warm-neutral cream or sand body backgrounds (#f5f1eb or anything in the OKLCH L 0.84–0.97, C < 0.06, hue 40–100 band). The dark editorial ground is identity; the cream background is the opposite of this brand.
- **Don't** introduce additional accent colors without a specific, documented purpose. Community Flame is the system's one warmth source. The robotics course uses Cyan (#55c7d9) and Green (#00aa6c) as secondary accents within its own panel — those are scoped to that section only and should not leak into the main site.
