# 🧃 GOOD AS HELL INSIDE & OUT — Tropicana × Lizzo

Bold new prebiotic soda campaign site. Built as a single-page experience.

---

## 🚀 Deploy to Vercel (3 ways)

### Option A — Vercel CLI (fastest)

```bash
# 1. Install Vercel CLI (if not already installed)
npm i -g vercel

# 2. From this folder, run:
vercel

# 3. Follow the prompts. On first deploy it will ask:
#    - Link to existing project? → N
#    - Project name: tropicana-lizzo (or anything)
#    - In which directory is your code? → ./  (press Enter)
#    - Want to override settings? → N

# 4. Your site is live! Copy the URL it prints.
```

### Option B — Vercel Dashboard (drag & drop)

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click **"Import"** → choose **"Continue with..."** to sign in (GitHub / GitLab / email)
3. On the dashboard click **"Add New → Project"**
4. Scroll down and click **"Deploy from your computer"**
5. Drag this entire folder (containing `index.html` + `vercel.json`) into the upload box
6. Click **Deploy** — your site will be live in ~30 seconds

### Option C — GitHub + Vercel (recommended for ongoing updates)

```bash
# 1. Create a new GitHub repo and push this folder
git init
git add .
git commit -m "initial deploy"
git remote add origin https://github.com/YOUR_USER/tropicana-lizzo.git
git push -u origin main

# 2. Go to vercel.com → "Add New Project" → Import from GitHub
# 3. Select your repo → Deploy
# 4. Every future `git push` auto-deploys ✅
```

---

## 📁 File Structure

```
tropicana-lizzo/
├── index.html      ← The entire site (self-contained)
├── vercel.json     ← Vercel config (headers, caching, rewrites)
└── README.md       ← This file
```

---

## ⚙️ What's Configured in vercel.json

| Feature | Setting |
|---|---|
| Clean URLs | `cleanUrls: true` (no .html in URL) |
| Trailing slash | Disabled |
| Security headers | X-Frame-Options, X-XSS-Protection, Referrer-Policy, Permissions-Policy |
| HTML caching | `no-cache` (always fresh) |
| Asset caching | 1 year immutable for JS/CSS/fonts |
| Image caching | 24 hrs + stale-while-revalidate |
| SPA fallback | All routes → index.html |

---

## 🌐 Custom Domain (optional)

After deploying on Vercel:
1. Go to your project → **Settings → Domains**
2. Add your domain (e.g. `goodashellsoda.com`)
3. Update your DNS at your registrar:
   - Add a **CNAME** record: `www` → `cname.vercel-dns.com`
   - Add an **A** record: `@` → `76.76.21.21`
4. Vercel auto-provisions SSL — live in minutes

---

## 🔧 Update the OG Image URL

Before deploying, update these two lines in `index.html` to match your actual Vercel URL:

```html
<link rel="canonical" href="https://YOUR-PROJECT.vercel.app/"/>
<meta property="og:url"   content="https://YOUR-PROJECT.vercel.app/"/>
<meta property="og:image" content="https://YOUR-PROJECT.vercel.app/og-image.png"/>
<meta name="twitter:image" content="https://YOUR-PROJECT.vercel.app/og-image.png"/>
```

---

## ✅ Production Checklist

- [x] Mobile cursor restored (`cursor:auto` on touch devices)
- [x] Custom cursor hidden on mobile
- [x] `prefers-reduced-motion` respected
- [x] Focus-visible outlines for keyboard accessibility
- [x] SEO meta tags (title, description, canonical)
- [x] Open Graph tags (Facebook, LinkedIn)
- [x] Twitter Card tags
- [x] Emoji favicon + Apple touch icon
- [x] Security headers via vercel.json
- [x] Font preconnect for faster load
- [x] Aggressive asset caching
- [x] Magnetic + parallax JS guarded for touch devices
- [x] `cursor:none` stripped on mobile
- [x] SPA 404 fallback configured

---

Built with 🧃 Tropicana × Lizzo energy.
