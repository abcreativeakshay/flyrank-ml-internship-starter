# Three Roads — Stack Rationale

## The constraint first

Everything here is **free-only**. No paid hosting, no paid domain extras, no paid APIs. Whatever I choose has to cost ₹0 to run and keep running.

## Road taken: static HTML/CSS on GitHub Pages

One self-contained HTML page (plus case pages as needed), inline CSS, no build step, no JavaScript framework, hosted on GitHub Pages from this repository.

- **Why it wins:** the page is a file. I can open it, read every line, and explain every line — which matters when the portfolio itself is the proof of skill. GitHub Pages is free, the deploy is `git push`, and there is nothing to patch, update or pay for. The contact form posts to a free form endpoint (FormSubmit) instead of needing a backend.
- **What I give up:** no server-side anything. No login, no database, no dynamic content. For a portfolio that is a feature, not a loss — there is nothing here that needs a server.

## Road not taken: Next.js on Vercel

- **What it offers:** component structure, fast image handling, easy forms and analytics, room to grow into a real app.
- **Why not:** it solves problems this site doesn't have. A build pipeline, a framework's worth of dependencies and a deployment platform between me and a page that is, at the end, text and links. If the portfolio ever becomes a product, this is the road I would switch to — and I would be switching with my eyes open, not by default.

## Road not taken: WordPress

- **What it offers:** a familiar editor, themes, plugins for forms and SEO.
- **Why not:** the free tiers limit exactly the control this exercise is about — custom design, my own palette and fonts, clean HTML I can explain. It also adds ongoing maintenance (updates, plugin health, security) to a page that should need none, and the result tends to look like the theme, not like me.

## The deciding sentence

The portfolio's job is to prove I can build and explain things myself — so the stack is the one where every line on the page is mine, it costs nothing, and `git push` is the whole deployment.
