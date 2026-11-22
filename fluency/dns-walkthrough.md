# PF-04 — How My Page Is Hosted Free on GitHub Pages (and what DNS is)

*Akshay Biradar — in my own words.*

## What I actually have running

My capstone paper and portfolio page are live at
**https://abcreativeakshay.github.io/flyrank-ml-internship-starter/portfolio/**
and I pay nothing for it. The hosting is GitHub Pages, which is free for public repos.

The setup, exactly as it is on my repo (`abcreativeakshay/flyrank-ml-internship-starter`):

1. The site files (the paper and the portfolio page, plain HTML) live in the **`/docs` folder** of the repo.
2. In the repo: **Settings → Pages → Build and deployment → Deploy from a branch**, with branch **`main`** and folder **`/docs`**.
3. Every time I push to `main`, GitHub rebuilds and republishes the site automatically. There is no server for me to manage, no FTP, nothing to install — a push is the deploy.
4. GitHub also gives the site HTTPS automatically on the `github.io` address, so the padlock works with zero effort from me.

The address itself tells the story: `abcreativeakshay` (my username) + `github.io` (GitHub's domain) + the repo name as the path.

## What DNS is, in plain words

DNS is the internet's phone book. Computers reach each other by IP addresses — strings of numbers like `185.199.108.153`. Nobody wants to type numbers, so DNS translates a name a human can remember (like `akshay.peakso.in`) into the IP address of the machine that serves it. When someone types my domain, their browser asks DNS "where does this name live?", gets an IP back, and connects there. The name is mine; DNS is just the directory that points the name at a host.

Right now my Pages site does not need any DNS work from me, because it lives under GitHub's own `github.io` name — GitHub's DNS already points that at GitHub's servers.

## If I later point a custom domain at it

Say I buy a domain and want the site at my own address instead of `github.io`. The steps would be:

1. **In the repo:** Settings → Pages → Custom domain → enter the domain (e.g. `www.my-domain.com`) and save. GitHub writes a `CNAME` file into the repo for me.
2. **At my domain registrar's DNS settings:**
   - For a `www` subdomain: add a **CNAME record** — host `www`, value `abcreativeakshay.github.io`.
   - For the bare apex domain (no `www`): add **A records** pointing to GitHub Pages' published IP addresses (GitHub lists them in its Pages documentation — I would copy them from there at the time, not from memory).
3. **Wait for DNS to propagate** — minutes to a few hours. Nothing is broken while it spreads; the old `github.io` address keeps working.
4. **Turn on "Enforce HTTPS"** in the same Pages settings once the certificate shows as issued (GitHub provisions a free Let's Encrypt certificate for custom domains). Until the certificate is ready, that checkbox stays greyed out — that is normal, not an error.

Two honest notes: buying the domain itself is the only paid step in this whole walkthrough, and I have **not** done it — the free `github.io` address is enough for the internship. And DNS changes are easy to get subtly wrong (one wrong record and the name points nowhere), so I would change one record at a time and check after each change.
