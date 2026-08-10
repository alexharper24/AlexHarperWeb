# Harper Studio — harperstudio.co

Marketing site for Harper Studio, Alex Harper's web design and care business
(New Albany, IN). Static HTML/CSS/JS, no build step, hosted on **GitHub Pages**
with the custom domain **harperstudio.co**.

## Editing

Everything is plain files — open an `.html` file, edit, commit, push. GitHub
Pages redeploys automatically from the `main` branch. There is no framework,
bundler, or install step.

> **Keep pages at the repo root.** The live URLs are flat
> (`/services.html`, `/plans.html`, …) and are indexed and listed in
> `sitemap.xml`. Moving a page into a subfolder changes its public URL and
> breaks SEO and existing links.

Run `python ../site-checks/check_site.py .` before committing; the same checks
run enforcing in CI on every push. Bump `?v=` on `studio.css` in the same
commit that changes it.

## Structure

| File | Purpose |
|------|---------|
| `index.html` | Homepage: hero, values, persona doors, services, pricing, process, work, FAQ teaser |
| `services.html` | Services overview (hub) |
| `websites.html` / `hosting.html` / `domains.html` | Service detail pages |
| `plans.html` | Care plan comparison (build from $1,200; plans $45 / $95 / from $225) |
| `essential.html` / `standard.html` / `premium.html` | Care plan detail pages |
| `work.html` | Portfolio: four live client sites |
| `work-calvary-road.html` | Calvary Road case study (platform migration) |
| `faq.html` | FAQ with `FAQPage` schema |
| `about.html` | About Alex |
| `contact.html` | Contact form (FormSubmit.co, posts in background) |
| `thank-you.html` | No-JS form fallback landing |
| `privacy.html` | Privacy policy |
| `terms.html` | Redirect stub to `plans.html` (old URL preserved) |
| `404.html` | Not-found page (root-relative links, by design) |
| `studio.css` | All styles; design tokens in the two `:root` blocks |
| `sitemap.xml`, `robots.txt`, `CNAME`, `.nojekyll` | Hosting + SEO plumbing |
| `img/`, `assets/` | Images and brand assets (`img/services/source/` is gitignored) |
| `notes/` | **Gitignored.** Market assessment + action plan (internal, never published) |
| `tools/` | Local helper scripts |

## Conventions

- Prices shown on the site are the live offer: build from $1,200 one-time;
  Essential $45 / Standard $95 / Premium from $225 per month; church and
  nonprofit rate $30 / $75 / from $175. Update `plans.html`, the three detail
  pages, `faq.html`, and the homepage pricing section together.
- Header nav and footer are duplicated in every page. Change one, change all,
  then grep to confirm. `404.html` uses root-relative hrefs; every other page
  is relative.
- Analytics: GA4 (`G-X2Q4TFJQM4`) and Cloudflare Web Analytics on every page.
- Contact form posts to FormSubmit.co with `_honey` honeypot; JS submits in the
  background and reveals `#formSent`.

## Pending

- [ ] **Phase 2 decisions from Alex** (see `notes/action-plan.md`): start year +
      project count to claim publicly, written guarantee terms, turnaround
      commitment, Starter tier price/contents, whether Starter requires a plan.
      The FAQ timeline answer gets a concrete number once turnaround is decided.
- [ ] **Testimonials**: ask all four clients for a short written quote; first
      one goes in the `.hero-quote` component already built in `studio.css`.
- [ ] **Google Business Profile**: stand up, then begin the review flywheel.
- [ ] **Pricing correction** (barbell: Starter / Signature / Advanced + raised
      care plans) ships with the Phase 2 decisions, not before.
- [ ] Character pass (Phase 3): hand-drawn gold-line motif, voice pass, single
      repeated CTA everywhere.
