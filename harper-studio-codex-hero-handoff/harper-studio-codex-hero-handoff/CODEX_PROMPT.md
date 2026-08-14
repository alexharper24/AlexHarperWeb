# Harper Studio Homepage Hero — Codex Implementation Prompt

Work in the existing Harper Studio repository. Before changing code, inspect the project structure, homepage, header/nav implementation, global styles/theme tokens, responsive breakpoints, fonts, and existing components.

## Goal
Rebuild **only the homepage header + hero** so the rendered desktop page visually matches:

`design-reference/hero-target.png`

Use this file only as a visual reference. Do not render the reference image on the website.

Use the actual hero background asset:

`public/images/hero/harper-hero-cinematic.webp`

The PNG source is also available at:

`public/images/hero/harper-hero-cinematic.png`

For comparison, the previous unsuccessful implementation is saved at:

`design-reference/current-implementation.png`

## Non-negotiable layout rules

1. Keep the existing warm paper/off-white page background.
2. The header/nav is a **separate normal-flow banner above the hero**, not overlaid on the image.
3. The header inner content and hero outer edges should share the same centered page alignment.
4. The hero must have visible left/right page gutters like the target reference.
5. The hero must be one photographic background surface, not a two-column text + image layout.
6. Use the supplied hero image as a CSS background with `background-size: cover`.
7. Add a dark-to-transparent horizontal overlay on the left side of the photograph.
8. Place the hero text as an overlay above the background on the left side.
9. Keep the right side primarily photographic: plant, mug, laptop, notebook should remain visible.
10. Keep the rounded hero corners and restrained shadow seen in the target.
11. Preserve the existing Harper Studio copy, logo, typography, links, and brand colors unless a tiny spacing/color adjustment is required for contrast.
12. Do not redesign any sections below the hero.

## Desktop geometry target

At a desktop viewport around 1440–1600px wide:

- Header inner width: aligned with hero width.
- Hero outer width: roughly `min(1420px, calc(100% - 96px))`.
- Hero left/right gutter: approximately 48px on large screens, scaling down responsively.
- Hero border radius: approximately 12–16px.
- Hero min-height: approximately `calc(100svh - 150px)`; tune visually rather than forcing an exact number.
- Hero copy max-width: approximately 500–540px.
- Hero content left inset: approximately 6–7% of the hero width.
- Hero copy vertically centered with a slight upward bias.
- Background position starting point: around `60% center`; visually tune between roughly 56–64% until laptop/mug/notebook match the reference proportions.

## Required visual composition

The target should read visually as:

- dark cinematic shadow on the left
- smooth transition through the center
- clear warm photography on the right

Do not make the overlay look like a flat brown rectangle.

A good starting gradient is:

```css
background: linear-gradient(
  90deg,
  rgba(12, 17, 20, 0.94) 0%,
  rgba(15, 19, 22, 0.90) 22%,
  rgba(20, 22, 23, 0.77) 36%,
  rgba(28, 27, 24, 0.56) 48%,
  rgba(34, 30, 24, 0.28) 58%,
  rgba(34, 30, 24, 0.08) 68%,
  rgba(34, 30, 24, 0) 76%
);
```

Tune this against the actual screenshot rather than treating these values as fixed.

## Header requirements

The header should remain a clean warm/cream banner in normal document flow.

- No giant gap between header and hero.
- No dark hero image behind the header.
- No floating glass card treatment.
- Keep existing logo and nav labels.
- Keep existing rust/orange consultation CTA.
- Keep header content centered and aligned with the hero.

## Hero content

Preserve the repository’s existing homepage content, including the current:

- eyebrow
- headline
- body copy
- proof statement
- primary CTA
- secondary CTA
- service pills

Do not rewrite copy unless the repository differs from the target because of an obvious stale test string.

### Styling target

- Eyebrow: warm gold, handwritten/script styling already used by the site.
- Headline: cream/white serif, dominant visual priority.
- Body: muted warm white.
- Proof line: small uppercase, muted warm cream/gold, restrained tracking.
- Primary CTA: rust/orange.
- Secondary CTA: transparent/dark translucent with a light border.
- Service pills: low-emphasis translucent dark/neutral surfaces, subtle borders, warm-gold icons.

Avoid SaaS-style glassmorphism, excessive glow, oversized shadows, or generic gradients.

## Recommended structural approach

Use the existing framework and components, but conceptually the hero should behave like:

```html
<header class="site-header">
  <div class="nav-inner">...</div>
</header>

<main>
  <section class="hero-shell">
    <div class="hero-photo">
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <div class="hero-copy">...</div>
      </div>
    </div>
  </section>
</main>
```

Do not use an `<img>` as a right-hand grid column for the desktop hero.

## Responsive behavior

### Tablet
- Reduce outer gutters.
- Preserve the background-photo hero treatment.
- Increase overlay strength slightly if needed for readability.
- Keep the copy comfortably readable without covering the laptop.

### Mobile
- Keep the hero as a photographic background, not a boxed two-column conversion.
- Reduce gutters to around 10–16px.
- Increase overlay coverage/darkness as needed.
- Reposition the background so the laptop/plant still create context without fighting the text.
- Let buttons stack if needed.
- Let service pills wrap.
- Preserve comfortable headline sizing and line-height.

## Visual validation loop — required

Do not stop when the CSS merely compiles.

Run the site locally and compare the rendered desktop homepage to:

`design-reference/hero-target.png`

Iterate on these variables until the result is visually close:

- header height
- header/hero shared alignment
- hero width
- hero height
- top spacing between nav and hero
- border radius
- shadow strength
- background position
- gradient stops/opacity
- hero copy left inset
- hero copy vertical position
- headline size and wrapping
- paragraph width
- CTA sizing
- service-pill size/opacity

Use browser screenshots if your environment supports them. The target is visual similarity, not just semantic equivalence.

## Acceptance checklist

Before finishing, verify all of these:

- [ ] Page background remains warm/off-white.
- [ ] Header is separate above hero.
- [ ] Header and hero share centered alignment.
- [ ] Hero has visible left/right gutters.
- [ ] Hero is not a two-column layout.
- [ ] Supplied WebP is the live background image.
- [ ] Dark fade is strongest on left and nearly transparent before the laptop.
- [ ] Mug remains visible around the center-right.
- [ ] Laptop remains prominent but not oversized.
- [ ] Notebook remains visible at lower right.
- [ ] Text is clearly legible over the left side.
- [ ] Hero has rounded corners and subtle depth/shadow.
- [ ] No downstream homepage section was redesigned.
- [ ] Desktop layout is visually close to the target reference.
- [ ] Tablet and mobile are usable and intentional.
- [ ] No horizontal overflow.
- [ ] Existing links/buttons still function.
- [ ] Build passes.
- [ ] Lint/tests pass if configured.

## Final response

When complete, report:

1. Files changed.
2. Final hero width/max-width and gutters.
3. Final hero height/min-height.
4. Final background position.
5. Final overlay gradient.
6. Responsive breakpoint changes.
7. Build/lint/test results.
8. Any remaining visual difference from the target that you could not eliminate.
