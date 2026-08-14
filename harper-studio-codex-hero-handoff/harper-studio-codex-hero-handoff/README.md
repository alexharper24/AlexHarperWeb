# Harper Studio Codex Hero Handoff

This package is intended to be copied into the root of the Harper Studio repository before starting a fresh Codex task/chat.

## Included files

- `CODEX_PROMPT.md` — paste this into the new Codex chat/task.
- `design-reference/hero-target.png` — the exact visual target Codex should match.
- `design-reference/current-implementation.png` — the prior implementation that did not match well enough.
- `public/images/hero/harper-hero-cinematic.webp` — use this on the live website.
- `public/images/hero/harper-hero-cinematic.png` — high-quality source/fallback.
- `docs/HERO_SPEC.md` — extra visual/layout notes.

## How to use

1. Copy the contents of this package into the repository root, preserving the folders.
2. If files with the same names already exist, back them up or compare before overwriting.
3. Commit or save the files so Codex can see them in the repository/environment.
4. Start a fresh Codex chat/task with the Harper Studio repository selected.
5. Tell Codex: `Read CODEX_PROMPT.md and implement it. Inspect the existing app before editing, run it locally, and iterate visually against design-reference/hero-target.png.`
6. Let Codex inspect and run the project before making broad changes.
7. Review the rendered desktop result before accepting. If it is not visually close, ask Codex to continue the visual comparison loop rather than starting over.

## Important

The reference PNG is not a production asset. Do not place `hero-target.png` into the live page. The production hero should use `public/images/hero/harper-hero-cinematic.webp` plus HTML/CSS for the header, overlay, copy, CTAs, and service pills.
