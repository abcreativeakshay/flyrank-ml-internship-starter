# Explain It Like You Built It

This is my portfolio page — the one in `docs/portfolio/` — explained the way I would explain it to someone sitting next to me.

## What the page is

It is one single HTML file. Not a website built by a tool — one file I can open in any browser, and everything it needs is inside it. The styling is written in a `<style>` block in the same file, so there are no separate CSS files, no downloads, and nothing that can break because some other file moved.

## How it is put together, top to bottom

1. **The head** sets the basics: the page title, the character encoding, and one important line — the viewport tag — which tells a phone "show this at phone width." Without that line the page would render tiny on mobile and most of my visitors are on phones.
2. **The style block** holds my identity kit in code form: the warm charcoal background `#161210`, the amber accent `#f2a93b`, the warm off-white text, and the layout rules. Sections are spaced with margins, the cases sit in panels one shade lighter than the background, and a media query at the end stacks everything into a single column on narrow screens.
3. **The header** is my name and one line — the claim: I build AI systems that ship and get measured. That is the whole pitch; everything below it is evidence.
4. **The Cases section** is four blocks, one per project — COGNIVA, Kaagaz AI, the FlyRank ML capstone, and the DMDW warehouse work. Each block says the problem, what I built, and carries its real number where it has one: the capstone's Precision@50 of 0.68 against the 0.24 baseline is right there in the text, not hidden in a PDF.
5. **The About section** is three lines: who I am, where I study, where I work. Nothing more — anyone who wants the long version has LinkedIn.
6. **The Contact section** is a plain HTML form: name, email, message, and a submit button. The form's `action` points to FormSubmit (`https://formsubmit.co/abcreativeakshay@gmail.com`), a free service that turns a form submission into an email to me. That is the trick that lets a static page with no server still receive messages.
7. **The footer** links out: LinkedIn, GitHub, and my main site at akshay.peakso.in.

## Why it is built this way

Because I can explain every line of it. There is no framework doing magic I would have to hand-wave about in an interview, no build step that can fail, and hosting it costs nothing — GitHub Pages serves the file straight from the repo. If I want to change a word, I edit the file and push. The page is simple on purpose: the work is supposed to be the impressive part, not the container.
