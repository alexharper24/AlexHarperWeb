# Alex Harper — byalexharper.com

Marketing site for Alex Harper's web design & care business (New Albany, IN).
Static HTML/CSS/JS, no build step, hosted on **GitHub Pages** with the custom
domain **byalexharper.com**.

## Editing

Everything is plain files — open an `.html` file, edit, commit, push. GitHub
Pages redeploys automatically from the `main` branch. There is no framework,
bundler, or install step.

> **Keep pages at the repo root.** The live URLs are flat
> (`/services.html`, `/pricing.html`, …) and are indexed + listed in
> `sitemap.xml`. Moving a page into a subfolder changes its public URL and
> breaks SEO and existing links.

## Structure

| File | Purpose |
|------|---------|
| `index.html` | Homepage |
| `services.html` | Services overview |
| `work.html` | Portfolio / recent work |
| `pricing.html` | Care plan comparison |
| `contact.html` | Contact form |
| `terms.html` | Care plan & build terms |
| `essential.html` / `standard.html` / `premium.html` | Care plan detail pages ($30 / $75 / from $175 per mo) |
| `styles.css` | Site-wide styles (design tokens in `:root`) |
| `alex-headshot.jpg`, `og-image.png` | Images (headshot; social share card) |
| `robots.txt`, `sitemap.xml` | SEO |
| `.nojekyll` | Tells GitHub Pages to skip Jekyll and serve files as-is |

## Design tokens

Colors and fonts live in the `:root` block at the top of `styles.css`
(`--accent`, `--ink`, `--bg`, `--font`, …). Change them there to re-theme the
whole site.

## Notes

- The contact form (`contact.html`) needs a live form-handler endpoint before
  it will deliver messages.
