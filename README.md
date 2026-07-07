# Asking Why Until It Hurts — BornHack 2026

**Live deck:** https://nis2-talk.blacklog.net (dark theme at
[/dark.html](https://nis2-talk.blacklog.net/dark.html))

A 28-slide conference deck (1920×1080) for a 45-minute BornHack talk on NIS2
compliance as a change-management problem. Terminal/hacker aesthetic: dark
background, faint green grid, monospace commands, green accent.

The deck is plain static HTML — no build step. `site/dark.html` contains all
28 slides and is the editable source; `site/deck-stage.js` provides the
presentation shell (scaling, arrow-key navigation, thumbnail rail,
print-to-PDF).

Two themes are served:

- `/` — "Milky Matcha" light theme, the default (the talk runs on a
  projector in a daylight tent). Generated from the dark deck by
  `scripts/make-light.py` — re-run it after editing `site/dark.html`.
- `/dark.html` — the original dark terminal theme (screens, dim rooms)

## View locally

Any static file server works:

    python -m http.server 8080 --directory site

Open http://localhost:8080

## Build & run with Docker

    docker build -t asking-why .
    docker run -d -p 8080:80 asking-why

Open http://localhost:8080

## Publish via GitHub Actions

`.github/workflows/docker-publish.yml` builds and pushes the image to Docker
Hub on every push to `main` (plus manual runs via workflow_dispatch).

One-time setup on this GitHub repo:

1. On Docker Hub: Account Settings → Personal access tokens →
   Generate new token (Read & Write).
2. Repo Settings → Secrets and variables → Actions → add:
   - `DOCKERHUB_USERNAME` — your Docker Hub username
   - `DOCKERHUB_TOKEN` — the access token from step 1

The image lands at `YOUR_USER/asking-why:latest` plus a per-commit sha tag.

## Presenting

- ←/→ arrow keys to navigate slides; 1–9/0 jump to slide, Home/End for first/last.
- Press F to toggle fullscreen presentation mode (hides the thumbnail rail
  and nav overlay); Esc or F again to exit.
- Use the browser print dialog for a one-page-per-slide PDF.
- Fonts (JetBrains Mono, Space Grotesk) load from Google Fonts at runtime,
  so presenting needs internet access. Everything else is served locally.

## Design

The original design handoff (slide inventory, design tokens, layout specs) is
in [docs/DESIGN_HANDOFF.md](docs/DESIGN_HANDOFF.md). `site/dark.html` is the
source of truth for all visual decisions — colors, typography, spacing, and
copy are final.
