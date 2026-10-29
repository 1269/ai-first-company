# AI-First Company

> A framework for building a company with AI at the center — from finding your niche to shipping a product, with real projects built in public.

This isn't theory. It's a documented methodology for building a business and its products using AI-native workflows — finding where AI solves real pain, validating an offer before you build, prototyping in weekends, shipping MVPs in weeks, and marketing before the product is done.

This repo is the open-source companion to my [YouTube channel](https://youtube.com/@jashia), where I build real apps and agents in public and teach the frameworks behind them.

Clone this repo. Run the commands. Build your AI-first business.

---

## Two Tracks

The repo has two tracks that work together:

- **Start the business** (phases 0–3): find your niche, design an offer people will pay for, stand up your agents and automations, and go to market. Every phase has guides, copy-paste prompts, and Claude Code commands. Ready to use today.
- **Build the product** (5 stages): take one idea from problem to prototype to MVP to launch to growth. Each stage gets a guide, templates, and a case study from a project built on the channel. Being written as the videos come out.

### Start the business: 4 phases

```
Phase 0: Discover    →  Who are you? What do you know? Where's the pain?
Phase 1: Validate    →  Will people pay for this? How much? How do you price it?
Phase 2: Build       →  Tech stack, agents, automations, infrastructure
Phase 3: Launch      →  Content engine, lead gen, go-to-market
```

Each phase has:
- **Guides** — Strategic context and frameworks for decision-making
- **Prompts** — Copy-paste prompts you can use in any AI assistant
- **Commands** — Pre-built slash commands for Claude Code (`.claude/commands/`)

### Build the product: 5 stages

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  IDEA    │───▶│PROTOTYPE │───▶│   MVP    │───▶│ LAUNCH   │───▶│  GROW    │
│          │    │          │    │          │    │ & TRACK  │    │          │
│ Problem  │    │ Working  │    │ Scoped   │    │ Ship it, │    │ Real     │
│ worth    │    │ demo in  │    │ product  │    │ measure  │    │ numbers, │
│ solving  │    │ a weekend│    │ people   │    │ every-   │    │ real     │
│          │    │          │    │ can use  │    │ thing    │    │ decisions│
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
```

| # | Guide | Stage | Status |
|---|-------|-------|--------|
| 1 | [Idea to Prototype](framework/01-idea-to-prototype.md) | Prototype | Available |
| 2 | Prototype to MVP | MVP | Coming soon |
| 3 | Marketing Before Launch | Launch | Coming soon |
| 4 | Analytics From Day One | Track | Coming soon |
| 5 | Reading Your Metrics | Grow | Coming soon |

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/1269/ai-first-company.git
cd ai-first-company

# 2. Follow the install guide
cat INSTALL.md

# 3. Start with Phase 0: Discover your niche
cat 00-discover/skills-audit.md
```

For detailed setup instructions, see **[INSTALL.md](INSTALL.md)**.

## What's Inside

```
ai-first-company/
├── README.md                     # You are here
├── INSTALL.md                    # Get up and running
├── MY_NICHE_TEMPLATE.md          # Your niche, offer and customer on one page
│
├── 00-discover/                  # Find your niche
│   ├── skills-audit.md
│   ├── market-fit.md
│   ├── niche-generator.md
│   └── prompts/
│
├── 01-validate/                  # Validate before building
│   ├── offer-design.md
│   ├── ideal-customer.md
│   └── prompts/
│
├── 02-build/                     # Stand up your infrastructure
│   ├── tech-stack.md
│   ├── automation-playbooks.md
│   └── prompts/
│
├── 03-launch/                    # Go to market
│   ├── content-engine.md
│   ├── lead-gen.md
│   └── prompts/
│
├── agents/                       # AI agent configs & templates
│   └── templates/
│
├── guides/                       # Deep-dive reference material
│
├── framework/                    # Build the product: the 5-stage guides
├── templates/                    # Copy-paste files for your own projects
├── case-studies/                 # Real projects built in public with real numbers
├── resources/                    # Business strategy and AI readiness materials
│
├── .claude/commands/             # Claude Code slash commands
└── .cursor/rules/                # Cursor AI rules
```

### Templates

| Template | What It's For | Status |
|----------|--------------|--------|
| [Project Structure](templates/project-structure/) | Scaffold for an AI-first project | Available |
| [Lead Research Agent](agents/templates/lead-research-agent/) | Researches a prospect and drafts outreach context | Available |
| MVP Checklist | Readiness checklist before shipping | Coming soon |
| Marketing Plan | Pre-launch marketing template | Coming soon |
| Analytics Config | Starter tracking setup | Coming soon |

---

## Using the Commands

### Claude Code

The `.claude/commands/` directory contains slash commands you can use directly:

```bash
# In Claude Code, just type:
/discover-niche
/audit-skills
/design-offer
/generate-agent
```

### Cursor / Other AI Assistants

Copy the prompts from any `prompts/` directory and paste them into your assistant. They're written to be tool-agnostic.

### Manual / Any LLM

Every prompt file works as a standalone. Copy the contents, paste into ChatGPT, Gemini, Claude.ai, or any LLM of your choice.

## Guides

In-depth reference material for key topics:

| Guide | What It Covers |
|-------|---------------|
| [GPS Framework](guides/gps-framework.md) | Goal → Plan → System methodology for any initiative |
| [12-Week Year](guides/12-week-year.md) | Sprint-based quarterly execution |
| [AI Tool Landscape](guides/ai-tool-landscape.md) | Current best tools and when to use each |
| [Pricing AI Services](guides/pricing-ai-services.md) | Value-based pricing for AI consulting & products |

---

## Core Principles

1. **AI-First, Not AI-Added** — Every process starts with "how would an AI handle this?" before "how would a human handle this?"
2. **Ship Before Perfect** — A working agent that runs today beats a perfect system that launches never.
3. **Automate What Repeats** — If you do it 3+ times, it should be a workflow, not a task.
4. **Value Over Volume** — Price on outcomes, not hours. Charge for the transformation.
5. **Stay Lean** — Solo operators with AI leverage can outperform teams of 10. Don't hire until it hurts.

## The GSD Framework

**GSD (Get Shit Done)** is the methodology behind the product track. It's how one person (or a small team) ships real products using AI as a force multiplier.

The core idea: AI doesn't replace your judgment — it accelerates your execution. You still decide what to build and why. AI helps you build it faster, test it sooner, and iterate without burning out.

**Principles:**
- **Ship, don't plan** — A working prototype beats a perfect plan
- **Scope ruthlessly** — Cut everything that isn't essential to the first version
- **Market early** — Start building awareness before the product is done
- **Measure everything** — Set up tracking from day one, not after launch
- **Iterate in public** — Share the real numbers, the real decisions, the real mistakes

---

## Build in Public

This repo includes case studies from real projects built on the channel. Each one follows the full arc:

1. **The Prototype** — Idea to working demo
2. **Prototype to MVP** — Real decisions, scope cuts, what stays and goes
3. **Building the Marketing** — Digital marketing while the product is still being built
4. **Launch & Track** — Ship it, set up analytics, watch real metrics
5. **Retrospective** — Honest review of what worked, what didn't, what's next

Case studies will be added as videos are published.

---

## Who This Is For

- **Solo founders** who want to build and ship without a team of 10
- **Business owners** exploring AI but unsure how to start building
- **Consultants** looking to productize AI automation services
- **Engineers** who want to start an AI-focused side business or company
- **Side project builders** who have limited time and need to be ruthless about scope
- **Anyone** who's tired of tutorials that stop at "hello world"

## Contributing

If you've built an AI-first company (or are building one), your experience makes this better for everyone.

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for how to contribute guides, prompts, agent templates, or improvements.

## Related

- **[AI System](https://github.com/1269/ai-system)** — Build your personal AI productivity system
- **[YouTube Channel](https://youtube.com/@jashia)** — Weekly videos on building with AI

## License

[MIT](LICENSE) — Use it, fork it, build on it. Just go build something.

---

**Built by [Ja Shia](https://jashia.com) | [Through The Looking Glass](https://ttlg.ai)**

*Documenting the journey of building an AI-first company, one commit at a time.*
