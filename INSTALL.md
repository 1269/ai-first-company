# Installation Guide

Get up and running in under 5 minutes.

## Prerequisites

- **Git** — to clone the repo
- **An AI assistant** — Claude Code, Cursor, Gemini, Windsurf, or any LLM

That's it. No dependencies. No package managers. No build steps.

This is a framework of guides, prompts, and commands — not a software application.

## Step 1: Clone the Repo

```bash
git clone https://github.com/yourusername/ai-first-company.git
cd ai-first-company
```

## Step 2: Choose Your AI Assistant

### Option A: Claude Code (Recommended)

Claude Code has native support for the slash commands in this repo.

```bash
# Install Claude Code if you haven't already
npm install -g @anthropic-ai/claude-code

# Navigate to the repo
cd ai-first-company

# Start Claude Code — it will automatically detect .claude/commands/
claude
```

Once inside Claude Code, type `/` to see available commands:

```
/discover-niche    — Guided niche discovery session
/audit-skills      — Inventory your skills and experience
/design-offer      — Design your first offer using the Value Equation
/generate-agent    — Scaffold a new AI agent for your business
```

### Option B: Cursor

1. Open the `ai-first-company` folder in Cursor.
2. The `.cursor/rules/` directory will be automatically loaded.
3. Use the prompts from any `prompts/` folder by pasting them into the Cursor chat.

### Option C: Any Other AI Assistant

1. Open the repo in your file explorer or IDE.
2. Navigate to the phase you're starting with (e.g., `00-discover/`).
3. Open the prompt files and copy-paste them into your AI assistant of choice.

Every prompt is written as a standalone markdown file — no tool lock-in.

## Step 3: Start the Framework

Begin with Phase 0: Discover.

```bash
# Read the first guide
cat 00-discover/skills-audit.md

# Or if using Claude Code
/audit-skills
```

### Recommended Path

Follow the phases in order your first time through:

```
00-discover/skills-audit.md      →  What do you know?
00-discover/market-fit.md        →  Where's the pain?
00-discover/niche-generator.md   →  What's your niche?
          ↓
01-validate/offer-design.md      →  What's your offer?
01-validate/ideal-customer.md    →  Who are you serving?
          ↓
02-build/tech-stack.md           →  What tools do you need?
02-build/automation-playbooks.md →  What should be automated?
          ↓
03-launch/content-engine.md      →  How do you get seen?
03-launch/lead-gen.md            →  How do you get leads?
```

## Step 4: Make It Yours

This repo is your operating system. Customize it:

1. **Fork the repo** so you have your own copy.
2. **Add your own prompts** to the `prompts/` directories as you develop them.
3. **Drop agent configs** into `agents/templates/` as you build them.
4. **Contribute back** anything that would help others — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Updating

Pull the latest updates from the community:

```bash
git pull origin main
```

If you've forked, sync with upstream:

```bash
git remote add upstream https://github.com/yourusername/ai-first-company.git
git fetch upstream
git merge upstream/main
```

## Troubleshooting

**Q: Do I need to install Node.js / Python / anything?**
No. This is a collection of markdown files, prompts, and guides. If you use Claude Code, you'll need Node.js 18+ for Claude Code itself, but the framework has zero dependencies.

**Q: Can I use this with ChatGPT / Gemini / other LLMs?**
Yes. Every prompt is plain markdown. Copy and paste into any LLM.

**Q: I'm not technical. Can I still use this?**
Yes. The guides are written for anyone building a business. The prompts work by pasting text — no coding required. Start with the `00-discover/` phase and work through the guides.

**Q: How do I contribute?**
See [CONTRIBUTING.md](CONTRIBUTING.md). We welcome new prompts, guides, agent templates, and real-world case studies.

---

Ready? Start here: **[00-discover/skills-audit.md](00-discover/skills-audit.md)**
