# Open It on Your Phone — Fix Log (Akshay Biradar)

**Live URL:** https://abcreativeakshay.github.io/flyrank-ml-internship-starter/portfolio/

## What was checked

The portfolio page was built phone-first and checked at a narrow (phone-width) viewport before launch:

- `<meta name="viewport">` set, so the page renders at device width instead of a shrunk desktop layout.
- Single-column fluid layout — no fixed pixel widths, no horizontal scrolling at 360px.
- Cases stack vertically; headings and body text use relative sizes that stay readable without zooming.
- The contact form fields are full-width with large tap targets.
- No hover-only interactions: everything reachable by tap.
- No external assets, so the page loads fast on mobile data and cannot break if a CDN is down.

## Fix log

| # | Issue found in the first draft approach | Fix |
|---|---|---|
| 1 | Multi-column case grid would squeeze unreadably on a phone | Cases stack in one column under the small-screen breakpoint |
| 2 | Small footer links are hard to tap | Footer links given padding and separated tap areas |
| 3 | Form inputs at default size trigger auto-zoom on some phones | Input font-size set to 16px |

## Still mine to do

- Open the URL on my own phone and add a before/after phone screenshot here. The layout fixes above are real and live; the phone screenshot is the one piece of evidence only I can produce.
