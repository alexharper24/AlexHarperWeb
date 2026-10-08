---
name: alexharper-website-repo
description: Project state for Harper Studio, read first every session
kind: service-site
updated: 2026-10-07
gate: G5                    # set from seo-rollout.md; the live domain serves the holding page, see restore-main
review_url: ""
live_url: "https://harperstudio.co/"
context:
  nap: {name: "Harper Studio", phone: "+1-502-509-3105", email: "alex@harperstudio.co", area: "New Albany, IN 47150, service area only", source: published}
  service_area: {value: ["New Albany IN", "Jeffersonville IN", "Clarksville IN", "Louisville KY", "Southern Indiana"], source: published, note: "homepage schema areaServed; the profile lists Louisville, Clarksville and 3 other areas"}
  services: {value: ["website design and build", "website hosting", "domain and DNS management", "website care plans", "local SEO and Google Business Profile"], source: published}
  audiences: {value: ["churches", "nonprofits", "sole proprietors", "dog breeders"], source: confirmed, date: 2026-10-07, note: "Alex is open to any client but wants the most common work highlighted, which is churches and breeders"}
  conversion: {value: ["call or text", "contact form (FormSubmit)", "Let's Chat launcher"], source: confirmed, date: 2026-10-07, note: "every page always presents a way to reach Alex, same for every audience"}
  market: {value: ["northern Indiana", "the Midwest", "New Albany and Louisville as the home base"], source: confirmed, date: 2026-10-07, note: "target the region where the Warsaw-area work already sits; keyword pulls use the US database filtered to that region"}
  facts:
    - {fact: "Owner and sole designer is Alex Harper", source: published}
    - {fact: "Google Business Profile exists and is verified", source: confirmed, date: 2026-10-07}
    - {fact: "Live domain serves a noindex holding page from the maintenance branch since 2026-08-20, main is intact", source: confirmed, date: 2026-10-07}
    - {fact: "Search Console domain property sc-domain:harperstudio.co is verified", source: confirmed, date: 2026-10-07}
    - {fact: "Revenue comes mainly from one-time builds at first, so builds are the search focus; care plans stay on the site for now", source: confirmed, date: 2026-10-07}
    - {fact: "No numeric year-out targets; aim for what the keyword research and page work can reach", source: confirmed, date: 2026-10-07}
    - {fact: "What sets it apart, in Alex's words: someone who cares, does the job well, and pays attention to detail", source: confirmed, date: 2026-10-07}
    - {fact: "Keyword tool is the SE Ranking web app in Alex's Chrome (trial), not Semrush", source: confirmed, date: 2026-10-07}
    - {fact: "Business Profile has 2 Google reviews averaging 5.0 and no hours set", source: confirmed, date: 2026-10-07}
proposal: "hs-seo-data/alexharper/2026-10-07/proposal.md"
open:
  # added from this run
  - {id: restore-main, gate: G5, blocked_on: alex, item: "Decide when Pages goes back from the maintenance branch to main. Until then every page is noindex, robots.txt and sitemap.xml 404, analytics is off, and nothing on main (including the Let's Chat launcher) is live", proposal: "P12"}
  - {id: gsc-resubmit, gate: G5, blocked_on: claude, item: "After restore, resubmit sitemap.xml (last read 2026-08-18, Couldn't fetch) and request indexing for the priority pages", depends_on: [restore-main]}
  # G1 Discovery
  - {id: g1-old-site, gate: G1, blocked_on: claude, item: "Legacy URLs recorded (terms.html stub, the removed Infinite case study), NAP as the profile shows it, Search Console export", proposal: "P15"}
  - {id: g1-data, gate: G1, blocked_on: alex, item: "Connections recorded 2026-10-07 in hs-seo-data/alexharper/2026-10-07/manifest.json. Search Console read; Bing Webmaster Tools not confirmed; profile performance not yet read"}
  - {id: g1-money-searches, gate: G1, blocked_on: claude, item: "Keyword method run in full after g1-business", depends_on: [g1-data, g1-business]}
  - {id: g1-names, gate: G1, blocked_on: claude, item: "Variant check on service names", proposal: "P10"}
  - {id: g1-discovery, gate: G1, blocked_on: claude, item: "Keyword Magic broad match and Questions per service", proposal: "P11"}
  - {id: g1-serp-class, gate: G1, blocked_on: claude, item: "Page one for every proposed target, classified"}
  - {id: g1-competitors, gate: G1, blocked_on: claude, item: "Top three map-pack and top three organic competitors profiled", depends_on: [g1-money-searches]}
  # G2 Build
  - {id: g2-money-pages, gate: G2, blocked_on: claude, item: "One page per service, one buying term per page", depends_on: [g1-money-searches, g1-sales-by-entity]}
  - {id: g2-images, gate: G2, blocked_on: claude, item: "WebP with srcset and sizes, dimensions on every image, source media gitignored"}
  - {id: g2-house, gate: G2, blocked_on: claude, item: "Light-mode lock, ?v= cache-busting, lowercase relative paths, favicon set, 404 page, sitemap.xml and robots.txt"}
  # G3 Review
  # G4 Launch
  - {id: g4-noindex-off, gate: G4, blocked_on: alex, item: "noindex off and robots.txt open on the live domain. Main is clean; the live holding page is noindex,nofollow (curl 2026-10-07)", depends_on: [restore-main], proposal: "P3"}
  - {id: g4-search-consoles, gate: G4, blocked_on: alex, item: "Search Console verified (confirmed 2026-10-07); Bing Webmaster Tools not confirmed; sitemap needs resubmitting after restore"}
  - {id: g4-legacy-check, gate: G4, blocked_on: alex, item: "A sample of legacy URLs fetched and each lands on the right page", proposal: "P6"}
  - {id: g4-analytics, gate: G4, blocked_on: alex, item: "GA4 and Cloudflare Web Analytics are on every real page on main but not on the live holding page, so no visit count since 2026-08-20", depends_on: [restore-main], proposal: "P5"}
  # G5 Grow
  - {id: g5-gbp, gate: G5, blocked_on: alex, item: "Profile complete, website field pointing at the site, sameAs linked (done), Bing Places, Apple Business Connect", proposal: "P7, P8"}
  - {id: g5-nap-consistency, gate: G5, blocked_on: alex, item: "Site, schema, profile and directories match character for character (quarterly)", proposal: "P16"}
  - {id: g5-reviews, gate: G5, blocked_on: alex, item: "Review requests part of the handover routine and every review answered. Alex confirmed 2026-10-07 that asking at every handover is the goal and that several deployed sites have not reviewed yet; the profile holds 2 reviews"}
  - {id: g5-cluster, gate: G5, blocked_on: claude, item: "One content cluster in progress", depends_on: [g1-money-searches]}
  - {id: g5-links, gate: G5, blocked_on: alex, item: "Link work (quarterly)", proposal: "P9"}
  - {id: g5-ai-check, gate: G5, blocked_on: claude, item: "AI search visibility check (quarterly)"}
  - {id: g5-monthly, gate: G5, blocked_on: alex, item: "Monthly Search Console and profile check. First cache is 2026-10-07, so there is no earlier month to compare yet"}
closed:
  - {id: g1-business, closed: 2026-10-07, evidence: "Alex answered in chat: builds first, audiences churches, nonprofits, sole proprietors and breeders, market northern Indiana and the Midwest, no numeric targets, every page offers a way to reach him, differentiator is care and attention to detail. Recorded in context above"}
  - {id: g1-sales-by-entity, closed: 2026-10-07, evidence: "Alex answered in chat: clients with a real need sign fast once the value is explained; builds made unasked for a prospect, then pitched, stall because the prospect sees no need"}
  - {id: lets-chat-launcher, closed: 2026-10-07, evidence: "chat.js rebuilt in the Teapup and Sweet Puppy Paws format at Alex's request (close button, call or text with a text link, email, start, pricing, where; click outside closes), chat.js ?v=2; verified 320 to 1440 with every value aligned and the text link on the number's line"}
  - {id: g2-checks, closed: 2026-10-07, evidence: "dark-mode override shipped; site-checks e633f88 recognizes _honey, so harperstudio.co reports 0 errors and only the five by-design 404.html warnings"}
  - {id: infinite-case-study-url, closed: 2026-10-07, evidence: "work-infinite-solutions.html redirect stub to work.html (canonical, noindex follow, meta refresh, location.replace), out of sitemap.xml, listed in README, commit: Add the Infinite case study redirect, sitemap image entries and the dark-mode override"}
  - {id: g3-redirects, closed: 2026-10-07, evidence: "Local server 127.0.0.1 in the Browser pane: work-infinite-solutions.html lands on /work.html, terms.html and pricing.html land on /plans.html, commit: Add the Infinite case study redirect, sitemap image entries and the dark-mode override"}
  - {id: g2-sitemap-images, closed: 2026-10-07, evidence: "build_sitemap.py wrote 22 image entries across 5 pages (home 5, work 4, Calvary Road 6, Hope Baptist 6, about 1); sitemap.xml parses, commit: Add the Infinite case study redirect, sitemap image entries and the dark-mode override"}
  - {id: runbook-audit-out, closed: 2026-10-07, evidence: "seo-technical.md now passes --root and --out=<cache>/technical/audit-json and warns off --help; site-audit SKILL.md notes the ./audit default and the missing --help. Both files are outside this repo and not in git; recorded in commit: Add the Infinite case study redirect, sitemap image entries and the dark-mode override"}
  - {id: g2-onpage, closed: 2026-10-07, evidence: "audit.py on main at f1127db: all 18 sitemap pages have one H1, titles 23-60 characters, descriptions 82-153 characters, tel links on every real page (cache technical/audit-json)"}
  - {id: g2-schema, closed: 2026-10-07, evidence: "index.html carries ProfessionalService, WebSite and Person; every inner indexable page carries BreadcrumbList; all JSON-LD on 26 HTML files parses with json.loads, 0 errors"}
  - {id: g1-inputs, closed: 2026-10-07, evidence: "main carries the full site with name, phone, email, service area, logo and photos"}
  - {id: g1-context, closed: 2026-10-07, evidence: "context block above, from homepage schema and the README"}
  - {id: g1-baseline, closed: 2026-10-07, evidence: "SE Ranking Competitive Research US October 2026 holds no ranking searches for harperstudio.co, hs-seo-data/alexharper/2026-10-07/keywords/2026-10-07-baseline.md"}
  - {id: g1-design, closed: 2026-10-07, evidence: "character pass shipped 2026-08-09 per README"}
  - {id: g2-pages, closed: 2026-10-07, evidence: "websites, hosting, domains and local service pages plus about and contact on main"}
  - {id: g2-forms, closed: 2026-10-07, evidence: "contact form posts to FormSubmit.co per README"}
  - {id: g3-noindex, closed: 2026-10-07, evidence: "n/a, the site launched on its own domain with no separate public review copy"}
  - {id: g3-previews, closed: 2026-10-07, evidence: "the five preview pages on main carry meta robots noindex (grep 2026-10-07)"}
  - {id: g3-client-review, closed: 2026-10-07, evidence: "n/a, Alex's own business"}
  - {id: g4-dns-https, closed: 2026-10-07, evidence: "curl 2026-10-07: https apex 200, www and http both 301 to https apex. The certificate expires 2026-10-27 per README"}
decisions:
  - {date: 2026-10-07, decision: "Positioning set to churches, nonprofits and sole proprietors; Infinite Solutions removed from the site; Let's Chat launcher added (commit f1127db)"}
glossary:
  - {term: "Harper Studio", means: "the business", not: ["Harper Studios", "Harper Digital", "AlexHarperWeb"]}
  - {term: "the holding page", means: "the single page on the maintenance branch that Pages serves since 2026-08-20", not: ["maintenance site", "coming soon page"]}
  - {term: "care plan", means: "the monthly Essential, Standard and Premium plans", not: ["maintenance plan", "retainer"]}
  - {term: "Let's Chat launcher", means: "the chat.js contact button and panel with call or text, email and the form", not: ["live chat", "chatbot"]}
---

# Harper Studio

**Objective.** The site wins website work from churches, nonprofits and sole proprietors, and
done means it is live, indexed and measured, with one content cluster at a time.

**Status.** Main holds the full site with the 2026-10-07 positioning and the Let's Chat
launcher, but the domain has served a noindex holding page since 2026-08-20. The gate reads G5
from the rollout guide, while the G4 items for noindex, analytics and Bing stay open until
Pages points at main again.

## Open questions

The business-model questions and the restore decision are Alex's, and they are listed with
their task ids in `hs-seo-data/alexharper/2026-10-07/questions.md`.

## Next

Technical, local and content specialists read the 2026-10-07 cache. Keyword work waits on the
business-model answers.

## Where things landed

The SEO cache is at `C:\Git_Repos\hs-seo-data\alexharper\2026-10-07\`, which is never committed.
