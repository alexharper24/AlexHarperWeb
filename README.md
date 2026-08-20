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
| `websites.html` / `hosting.html` / `domains.html` / `local.html` | Service detail pages |
| `plans.html` | Build ladder, care plans, what's in/out of a build, scope definitions |
| `essential.html` / `standard.html` / `premium.html` | Care plan detail pages |
| `guarantee.html` | The six written commitments |
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

- Prices shown on the site are the live offer (set 2026-08-09): builds
  Starter $800 (1 page) / Complete $1,600 (up to 6 pages) / Signature from
  $2,400 (no page limit) / Advanced quoted, 25% deposit, revisions capped
  (1 round Starter, 2 rounds Complete and Signature); care plans
  Essential $65 / Standard $150 / Premium from $325 per month; church and
  nonprofit rate $45 / $100 / from $225. Starter is paired with a care plan.
  Existing clients keep their signed-up rates. Update `plans.html`, the three
  detail pages, `faq.html` (copy AND JSON-LD), and the homepage pricing
  section together.
- Turnaround commitment: Starter ~2 weeks after content is ready, Complete
  2-3 weeks, Signature 2-4 weeks. Stated on `websites.html`, `faq.html`, and
  `plans.html`; keep them in sync.
- **Scope definitions are load-bearing.** `plans.html` defines a revision
  round, an edit (Essential, 4/yr, ~30 min), and a request (Standard, 4/mo,
  ~1 hr, no rollover). `faq.html` repeats them in copy and JSON-LD, and the
  three plan detail pages restate their own. Change one, change all five.
- The written guarantee lives at `guarantee.html` (six commitments). Do not
  add promises there without Alex's sign-off.
- Header nav and footer are duplicated in every page. Change one, change all,
  then grep to confirm. `404.html` uses root-relative hrefs; every other page
  is relative.
- Analytics: GA4 (`G-X2Q4TFJQM4`) and Cloudflare Web Analytics on every page.
- Contact form posts to FormSubmit.co with `_honey` honeypot; JS submits in the
  background and reveals `#formSent`.

## Pending

- [x] ~~Phase 2 decisions~~ — resolved 2026-08-09: no tenure claim (honest "4
      live sites" proof line instead), guarantee shipped, turnaround published,
      Starter $800 with care plan required, plans $65/$150/$325.
- [ ] **Testimonials**: ask all four clients for a short written quote; first
      one goes in the `.hero-quote` component already built in `studio.css`.
- [x] ~~Google Business Profile~~ — already exists; the homepage `sameAs`
      already points at its Knowledge Graph id. Review asks are Alex's to run.
- [!] **Never add `Review` or `AggregateRating` schema to this site.** Checked
      against Google's review-snippet docs on 2026-08-17, and it is disqualified
      twice over, not once: a business that controls the reviews about itself
      makes its `LocalBusiness`/`Organization` pages "ineligible for star review
      feature", and separately "Don't aggregate reviews or ratings from other
      websites." Google states the restriction "applies whether reviews appear
      directly in structured data or through embedded third-party widgets", so a
      review widget carries the same penalty risk as hand-written JSON-LD. This
      supersedes the earlier note that said to add `AggregateRating` once reviews
      were real: real does not make it eligible. Stars in search come from the
      GBP itself, never from markup here. Displaying quotes on the page is fine;
      marking them up is not.
- [x] ~~GBP as a sellable service~~ — shipped 2026-08-09 as `local.html`:
      setup in every build, ongoing management and a monthly note on Standard
      and Premium, Essential explicitly excluded. **This is now a delivery
      commitment**: Standard/Premium clients expect their profile watched and
      a monthly note. Don't sell it without doing it.
- [x] ~~Pricing correction~~ — shipped 2026-08-09, four-rung build ladder plus
      raised care plans, with scope definitions and build exclusions published.
- [ ] **REMOVE THE LAUNCH OFFER AFTER 2026-12-31.** The "first three months of
      care included" band is live in **two** places: `plans.html` (full version
      with the reasoning) and `index.html` (short version in the pricing
      section), plus the `.offer` block in `studio.css`. It is deliberately
      dated in the copy so it cannot silently become permanent. Delete both
      bands, or extend the date in both, on or before that date.
      Deliberately **not** in `faq.html` or any JSON-LD, to keep the removal
      surface at two spots.
- [ ] **Testimonials: Alex is reaching out** (his four existing clients). First
      one drops into the `.hero-quote` component already built in `studio.css`.
      Never tie a discount to a testimonial or review: it violates Google's
      review policies and creates an FTC-disclosable material connection.
- [x] ~~Character pass (Phase 3)~~ — shipped 2026-08-09: `.hand-rule` and the
      `.steps.five` connector motif, voice pass, `.cta-or` call/text line on
      15 pages. **Keep the motif to three or four placements**; it stops being
      a signature and becomes decoration if it spreads.
- [ ] **Calvary before/after pair on the homepage** — the only Phase 3 item
      left, and it is blocked on Alex confirming which shots pair together.
      Never match photo pairs by visual inspection.
- [ ] Update the hero proof-line project count as new sites go live.

- **Case studies (added 2026-08-16, drafted from Internet Archive research):**
  `work-hope-baptist.html` and `work-infinite-solutions.html`. All claims are
  measured from archive captures or the live sites; review the copy before
  pointing clients at it. Open items:
  - Confirm the Infinite Solutions launch month (archive last captured the old
    WordPress site 2025-08-11; the rebuild launched sometime after, date not in
    copy until confirmed).
  - Before/after flip cards added 2026-08-16 from headless captures: Wayback
    `if_` snapshots for the befores, live sites for the afters. Both studies
    carry three cards (home, home-on-a-phone, and a subpage), matching Calvary.
    Infinite's phone-after needed a workaround for its X-Frame-Options
    SAMEORIGIN header: the live homepage HTML is fetched and framed from a local
    copy with a <base> tag pointing at the live origin, so the render uses the
    site's own live assets.

## Taken offline temporarily (2026-08-20)

GitHub Pages was disabled at Alex's request while he talks to businesses. The
site files are untouched; only the Pages deployment is off. `harperstudio.co`
DNS still points at GitHub, so requests now hit GitHub's own "no site here"
page rather than failing to resolve.

**To bring it back:** repo Settings, Pages, set Source to *Deploy from a branch*,
branch `main`, folder `/ (root)`. Then set the custom domain to `harperstudio.co`
and re-tick Enforce HTTPS once the certificate issues. Or by API:

    gh api -X POST repos/alexharper24/AlexHarperWeb/pages       -f "source[branch]=main" -f "source[path]=/"
    gh api -X PUT repos/alexharper24/AlexHarperWeb/pages -f cname=harperstudio.co -F https_enforced=true

The exact configuration as it was, for reference:

| Setting | Value |
|---|---|
| Source | branch `main`, path `/` |
| Custom domain | `harperstudio.co` |
| Enforce HTTPS | on |
| Custom 404 | yes (`404.html`) |
| Build type | legacy |
| Certificate | approved for `harperstudio.co` and `www.harperstudio.co`, was due 2026-10-27 |

**Two things to expect on restore.** The HTTPS certificate has to be re-issued,
which can take up to 24 hours, and Enforce HTTPS cannot be re-enabled until it
has. And the Search Console indexing work needs redoing: resubmit the sitemap and
re-request indexing, since pages served as errors while offline will have been
dropped.

**Left in place deliberately:** the "Site by Harper Studio" footer credits on
crbcindiana.com, hopebaptistwarsaw.org, and faithsblissfuldelights.com still
point at the domain, so those three links lead to a GitHub error page while this
is off. Alex chose to leave them. Reverting them is one commit per repo if that
changes.
