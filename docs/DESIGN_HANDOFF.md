# Handoff: BornHack 2026 talk deck — "Asking Why Until It Hurts"

## Overview
A 28-slide conference presentation (1920×1080) for a 45-minute BornHack talk on NIS2 compliance as a change-management problem. Terminal/hacker aesthetic: dark background, faint green grid, monospace commands, green accent. Three acts (The Easy Part / The Hard Part / Asking Why) with section dividers.

## About the Design Files
The files in this bundle are **design references created in HTML**. `deck.html` (a Design Component) is the source of truth for all visual decisions. Unlike an app prototype, this deck is also directly servable as static HTML — the included `docker/` folder ships it behind nginx with a GitHub Actions workflow for Docker Hub. If the task is instead to port it (e.g. to reveal.js, PPTX, or another framework), recreate the slides from the specs below using that environment's conventions.

## Fidelity
**High-fidelity.** Colors, typography, spacing, and copy are final. Recreate pixel-perfectly.

## Runtime structure
- `deck.html` — all 28 slides as inline-styled `<section data-label="…">` elements inside a `deck-stage` mount. No external CSS; every style is inline on the element.
- `deck-stage.js` — presentation shell web component: scaling to viewport, arrow-key navigation, thumbnail rail (drag to reorder), slide-count overlay, print-to-PDF (one page per slide). Not part of the design; any equivalent slide shell works.
- `support.js` — Design Component runtime used by our authoring tool. Only needed to open `deck.html` as-is; a port ignores it.

## Slide inventory (order matters)
1. **Title** — split layout: meta row top, 172px headline bottom-left, speaker footer
2. **whoami** — timeline 2023/2025/2026
3. **01 The Easy Part** — act divider (ghost numeral)
4. **The Assignment** — `$ cat brief.txt`
5. **The Reading List** — `$ ls ~/reading/` directory listing (nis2, iso-27001/2/5, iso-27035 pt 1–4, network/)
6. **The Mindset Behind the Rules** — `$ man nis2`
7. **Status Check** — `$ compliance --status`, [ done ]×3, [ pending ] implementation; act-1 punch
8. **02 The Hard Part** — act divider
9. **The Plan** — `$ ./implement.sh --dry-run`, [ ok ]×3
10. **The Plan in Production** — statement: "The plan only ever lived in plan mode." (`$ ./implement.sh --production` as amber kicker)
11. **The Logic Problem** — `$ ./convince.sh --method=logic`
12. **Mental Barriers of Change** — `$ dmesg | grep -i warn`, 8 warning cells W01–W08 in 2-col grid
13. **The Two Jobs of Implementation** — `$ jobs -l`, two bordered cards
14. **03 Asking Why** — act divider
15. **Change Management** — thesis statement slide
16. **The Reframe** — `$ diff pitch.old pitch.new` with `--- / +++` labels
17. **Find What Hurts** — `$ nmap --top-ports 5 organisation`, targets T01–T05
18. **Four Questions** — the core toolkit, numbered 01–04
19. **Until It Hurts** — `$ why --recursive` indented dialogue tree (└─)
20. **Upper Management Resistance** — `$ tail -f meetings/upper-management.log`, two-voice dialogue
21. **The Goal of the Journey** — ambition ladder, 4 ascending cards (0→3) with green color ramp
22. **What Changed** — `$ git log --oneline` with fake commit hashes
23. **The Incentives** — `$ echo $WHATS_IN_IT_FOR_ME`
24. **Know Your Role** — `$ id`, RESPONSIBILITY vs MANDATE definition blocks
25. **The Decay** — `$ dig manager.converted +ttl`
26. **The Heart of It** — Resilient / Documented / Reproducible at 110px
27. **Hearts and Minds** — takeaway, inverted: solid green bg, dark text
28. **Questions** — `$ why --interactive`, 160px headline

## Design tokens
Colors:
- Background: `#0c0e0c`; grid overlay: two `linear-gradient` layers `rgba(120,255,160,0.045)` 1px lines, `background-size: 96px 96px`
- Accent green: `#4dff88` (commands' punch lines, highlights, numbers)
- Amber (warnings/failure beats only): `#ffc857`
- Headline ink: `#eef2ee`; body: `rgba(220,235,224,0.82)`; muted/commands: `rgba(220,235,224,0.5)`; kickers: `rgba(220,235,224,0.4)`
- Inverted takeaway slide: bg `#4dff88`, ink `#071008`
- Ghost act numerals: `rgba(77,255,136,0.16)`

Typography:
- Headlines: Space Grotesk 700 (Google Fonts)
- Body/meta/commands: JetBrains Mono 400/700 (Google Fonts)
- Scale (px @1920×1080): cover title 172 (ls −5), act divider 130 + ghost numeral 380, slide title 96 (ls −2, lh 1.05), statements 110–140, big list items 110, body mono 36 (lh 1.5), commands 34, punch lines 34 green, kickers 24 (ls 3px, uppercase), card body 24–30

Layout:
- Slide: 1920×1080, padding 90px top/bottom, 110px sides, flex column
- Every content slide: kicker row (act tag left in green, running title right) → 96px title → command line → content → mono punch line
- Content gaps: 40–48px between list rows; 26px gap after `>` markers

## Interactions & Behavior
Presentation-only. deck-stage provides: ←/→ navigation, thumbnail rail, print-to-PDF. No other state, forms, or data fetching. Google Fonts load at runtime (needs network).

## Deployment (included)
`docker/` — `Dockerfile` (nginx:alpine serving `site/`), `README.md` (build/run/push instructions), `.github/workflows/docker-publish.yml` (build + push to Docker Hub on push to main; needs `DOCKERHUB_USERNAME` + `DOCKERHUB_TOKEN` secrets). Target repo: github.com/Reventlow/nis2_bornhack_2026.

## Assets
None — no images. All visuals are CSS (grid background, color ramp) and text.

## Files
- `deck.html` — the deck (source of truth)
- `deck-stage.js`, `support.js` — runtime to open it directly in a browser
- `docker/` — deployable package (site copy + Dockerfile + CI workflow)
