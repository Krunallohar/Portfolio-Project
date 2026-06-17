# B2B Newsletter & Email Marketing Research

---

## Topic
Newsletter and email marketing strategies for B2B SaaS companies.

---

## Why I Chose This Topic
Email and newsletters are the highest-leverage owned marketing channel in B2B SaaS. Unlike paid ads or social media, your email list is an asset you own. The best B2B SaaS companies — from HubSpot to Kit to Exit Five — have built their entire growth engine on the back of email.

I chose this topic because it sits at the intersection of strategy, copywriting, data, and product thinking — and because the gap between average and excellent is enormous and well-documented by real practitioners.

---

## Tools Used & Honest Constraints

I did not have a paid subscription to Claude Code or Codex. Instead of giving up, I found free alternatives to achieve the same outcome:

- **Cursor Agent (free tier)** — Used as my primary AI coding assistant throughout the project. Wrote scripts, organized files, and automated collection.
- **Python + youtube-transcript-api (free, no API key needed)** — Fetched real YouTube transcripts directly via API. Installed via pip.
- **Custom LinkedIn scraper (scrape_linkedin.py)** — Wrote and ran a Python scraper using requests + BeautifulSoup. LinkedIn blocked it with a login wall — expected and documented.
- **Manual collection (fallback)** — Visited each expert's public LinkedIn profile and copied posts directly. Both the scraper output and manual collection are preserved in the repo as proof of both approaches.
- **Multi-source expert research** — Used Reddit (r/SaaS, r/EmailMarketing), LinkedIn search, Substack leaderboards, newsletter directories, and cross-referencing who experts cite to find the right 10 people.

> The scraper didn't work. The manual method did. Both are in the repo. That's how real research works.

---

## How I Found the 10 Experts

I did not just Google "top email marketing experts." I researched across:
- Reddit communities — r/SaaS, r/EmailMarketing, r/marketing
- LinkedIn search for active B2B email practitioners with recent posts
- Substack leaderboards and newsletter directories
- Cross-referencing who other experts cite and recommend
- Podcast guest lists from top B2B marketing shows
- Parallel research using Claude and ChatGPT to validate selections

Priority was given to people who **actively run** high-performing newsletters or email programs — not just people who write about it.

---

## Experts Selected

| # | Name | What They Run | Why Selected |
|---|------|--------------|--------------|
| 1 | Emily Kramer | MKT1 Newsletter (40k+ subs) | Ex-Asana/Carta, treats newsletter as a standalone product |
| 2 | Dave Gerhardt | Exit Five (40k+ subs, community + podcast) | Ex-CMO Drift/Privy, most active B2B marketing voice |
| 3 | Samar Owais | Emails Done Right | SaaS email conversion specialist, lifecycle expert |
| 4 | Chenell Basilio | Growth in Reverse | Reverse-engineers how top newsletters actually grew |
| 5 | Val Geisler | Fix My Churn / Klaviyo | SaaS lifecycle email strategist, teardown expert |
| 6 | Corey Haines | SwipeFiles / Conversion Factory | SaaS marketing copywriting with real examples |
| 7 | Kipp Bodnar & Kieran Flanagan | Marketing Against the Grain | CMO/SVP at HubSpot & Zapier, enterprise-scale perspective |
| 8 | Jay Schwedelson | SubjectLine.com / Do This Not That | Analyzed 6B+ emails, pure data-driven expert |
| 9 | Nathan Barry | Kit (ConvertKit) | Built $30M+ company on newsletter craft |
| 10 | Lenny Rachitsky | Lenny's Newsletter (700k+ subs) | Largest paid B2B newsletter, gold standard |

---

## Repository Structure
/

├── README.md

├── fetch_transcripts.py              # Python script — fetches YouTube transcripts via API

├── scrape_linkedin.py                # Python script — LinkedIn scraper (blocked by login wall)

└── research/

├── sources.md                    # All 10 experts with links and annotations

├── linkedin-posts/

│   ├── Using_Scraper/            # Output from scrape_linkedin.py (login wall — empty content)

│   │   ├── emily-kramer.md

│   │   ├── dave-gerhardt.md

│   │   ├── samar-owais.md

│   │   ├── chenell-basilio.md

│   │   ├── val-geisler.md

│   │   ├── corey-haines.md

│   │   ├── kipp-bodnar.md

│   │   ├── jay-schwedelson.md

│   │   ├── nathan-barry.md

│   │   └── lenny-rachitsky.md

│   └── Using_Manually/           # Manual collection — real posts copied from public profiles

│       ├── emily-kramer.md

│       ├── dave-gerhardt.md

│       ├── samar-owais.md

│       ├── chenell-basilio.md

│       ├── val-geisler.md

│       ├── corey-haines.md

│       ├── kipp-bodnar.md

│       ├── jay-schwedelson.md

│       ├── nathan-barry.md

│       └── lenny-rachitsky.md

├── youtube-transcripts/          # Fetched via youtube-transcript-api (real transcript data)

│   ├── exit-five-how-to-do-better-email-marketing.md

│   ├── exit-five-email-teardown-2024.md

│   ├── jay-schwedelson-b2b-email-tips.md

│   ├── jay-schwedelson-email-subject-lines.md

│   └── jay-schwedelson-email-personalization.md

└── other/

├── newsletters-sampled.md    # 5 newsletters reviewed and analyzed

└── key-frameworks.md        # 6 frameworks synthesized from all research

---

## Scripts

### fetch_transcripts.py
- Fetches real YouTube transcripts using `youtube-transcript-api` (free, no API key)
- Successfully saved 5 transcripts from Exit Five and Jay Schwedelson videos
- Run with: `python fetch_transcripts.py`

### scrape_linkedin.py
- Attempts to scrape LinkedIn posts using `requests` + `BeautifulSoup`
- LinkedIn returns a login wall for unauthenticated requests — content blocked
- Output files created but contain login wall HTML, not post content
- Manual collection used as fallback — both approaches preserved in repo
- Run with: `python scrape_linkedin.py`

---

## Key Findings

1. **Newsletter as product** (Emily Kramer) — The best B2B newsletters have a clear POV, defined audience, and consistent format. They are not content distribution channels.

2. **Live text matters more than ever** (Jay Schwedelson) — AI email clients (Gmail Gemini, Apple Intelligence, Outlook Copilot) now summarize emails before humans read them. Content inside images is invisible to AI. Your most important message must exist as real HTML text.

3. **Reverse-engineer growth** (Chenell Basilio) — Study how successful newsletters grew rather than guessing. The growth tactics are always traceable and repeatable.

4. **Audience before product** (Nathan Barry) — Kit was built on the back of an engaged newsletter audience. Even a list of 1,000 has pilot clients and early adopters in it.

5. **Behavioral email beats broadcast** (Val Geisler / Samar Owais) — The best B2B SaaS email programs are built on lifecycle triggers, not batch-and-blast campaigns. Map the customer journey first.

6. **POV drives growth** (Dave Gerhardt / Emily Kramer) — Generic newsletters don't build loyal audiences. A strong point of view creates word-of-mouth and long-term retention.

---

## What's Next
This research will support a full B2B Newsletter & Email Marketing Playbook covering:
- How to launch a B2B SaaS newsletter from zero
- Growth tactics sourced directly from practitioners
- Email lifecycle frameworks for SaaS onboarding and retention
- Subject line and deliverability best practices based on real send data
