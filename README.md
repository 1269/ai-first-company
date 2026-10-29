# 🚀 AI-First Company

**An open-source framework for building a company with AI at the core — not bolted on as an afterthought.**

Clone this repo. Run the commands. Build your AI-first business.

---

## What Is This?

This is a step-by-step framework that helps you:

1. **Discover** your niche by auditing your skills and finding where AI solves real pain
2. **Validate** your offer before writing a single line of code
3. **Build** your infrastructure with AI agents, automations, and tools
4. **Launch** and go to market with a content engine and lead generation system

It's designed to work with any AI coding assistant — Claude Code, Cursor, Gemini, Windsurf, or whatever comes next. The prompts and commands are portable.

## Who Is This For?

- **Engineers** who want to start an AI-focused side business or company
- **Consultants** looking to productize AI automation services
- **Founders** building AI-native products from day one
- **Anyone** who wants to stop treating AI as a feature and start treating it as the foundation

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/ai-first-company.git
cd ai-first-company

# 2. Follow the install guide
cat INSTALL.md

# 3. Start with Phase 0: Discover your niche
cd 00-discover
cat skills-audit.md
```

For detailed setup instructions, see **[INSTALL.md](INSTALL.md)**.

## The Framework

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

### Directory Structure

```
ai-first-company/
├── INSTALL.md                    # Get up and running
├── README.md                     # You are here
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
│   ├── templates/
│   └── examples/
│
├── .claude/commands/             # Claude Code slash commands
├── .cursor/rules/                # Cursor AI rules
│
└── guides/                       # Deep-dive reference material
```

## Core Principles

1. **AI-First, Not AI-Added** — Every process starts with "how would an AI handle this?" before "how would a human handle this?"
2. **Ship Before Perfect** — A working agent that runs today beats a perfect system that launches never.
3. **Automate What Repeats** — If you do it 3+ times, it should be a workflow, not a task.
4. **Value Over Volume** — Price on outcomes, not hours. Charge for the transformation.
5. **Stay Lean** — Solo operators with AI leverage can outperform teams of 10. Don't hire until it hurts.

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

## Contributing

This is a community project. If you've built an AI-first company (or are building one), your experience makes this better for everyone.

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for how to contribute guides, prompts, agent templates, or improvements.

## License

MIT — Use it, fork it, build on it. Just go build something.

---

**Built by [Ja Shia](https://jashia.com) | [Through The Looking Glass](https://ttlg.ai)**

*Documenting the journey of building an AI-first company, one commit at a time.*
