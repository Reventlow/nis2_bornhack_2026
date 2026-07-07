# Asking Why Until It Hurts — BornHack 2026

A 28-slide conference deck (1920×1080) for a 45-minute BornHack talk on NIS2
compliance as a change-management problem. Terminal/hacker aesthetic: dark
background, faint green grid, monospace commands, green accent.

The deck is plain static HTML — no build step. `site/index.html` contains all
28 slides; `site/deck-stage.js` provides the presentation shell (scaling,
arrow-key navigation, thumbnail rail, print-to-PDF).

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

- ←/→ arrow keys to navigate slides.
- Press P or use the browser print dialog for a one-page-per-slide PDF.
- Fonts (JetBrains Mono, Space Grotesk) load from Google Fonts at runtime,
  so presenting needs internet access. Everything else is served locally.

## Design

The original design handoff (slide inventory, design tokens, layout specs) is
in [docs/DESIGN_HANDOFF.md](docs/DESIGN_HANDOFF.md). `site/index.html` is the
source of truth for all visual decisions — colors, typography, spacing, and
copy are final.
