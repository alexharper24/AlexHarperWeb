# Harper Studio Hero Visual Spec

## Source of truth

Visual target:
`../design-reference/hero-target.png`

Actual site image:
`../public/images/hero/harper-hero-cinematic.webp`

Previous failed attempt:
`../design-reference/current-implementation.png`

## What makes the target work

The hero is a single photo surface inside a centered, rounded container. The header is separate above it. The hero does not use a two-column layout. The left-side content is positioned over the same photo that continues behind the mug, plant, laptop, and notebook.

The dark treatment is a gradient overlay, not a separate dark box. It starts nearly opaque on the far left and becomes nearly transparent before the laptop.

## Approximate desktop proportions

- Page shell: warm off-white.
- Hero width: about 90–94% of viewport, with a practical max around 1420px.
- Large-screen gutters: about 48px.
- Hero radius: 12–16px.
- Hero height: nearly fills remaining viewport below header.
- Text width: about 500–540px.
- Text starts about 6–7% inside hero left edge.
- Text is vertically centered with a slight upward bias.
- Photography focal area occupies roughly the right 45–50%.

## Common failure modes to avoid

- White page header plus a full-bleed edge-to-edge hero when the target has gutters.
- Two-column layout with a separate `<img>` element.
- Brown rectangular overlay extending into the laptop.
- Hero copy centered in the left half instead of anchored to the page grid.
- Laptop enlarged so much that it dominates the composition.
- Service chips styled like primary controls.
- Large dead area below the buttons.
- Redesigning sections below the hero.
