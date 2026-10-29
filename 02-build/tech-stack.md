# Tech Stack

**Phase 2: Build → Step 1**

Time to build. But before you touch code, decide on your tools. The right stack for an AI-first solo operator looks different from a traditional startup.

## Guiding Principles

1. **Free or cheap until revenue.** Don't spend money you haven't earned.
2. **Managed over self-hosted.** Your time is better spent on the business than on DevOps.
3. **AI-native tools preferred.** Choose tools that have AI capabilities built in, not bolted on.
4. **Composable over monolithic.** Pick tools that integrate well. You'll be connecting everything.
5. **One tool per job.** Don't use Notion for tasks, notes, CRM, and wiki. Dedicated tools beat Swiss Army knives.

## Recommended Stack

This is a starting point. Adapt to your niche, not the other way around.

### Core Infrastructure

| Category | Recommended | Why | Cost |
|----------|------------|-----|------|
| **AI Coding Assistant** | Claude Code, Cursor, or Windsurf | Your primary development tool. Pick one and go deep. | $20-100/mo |
| **AI API** | Anthropic Claude or OpenAI | For building agents and automations. | Pay-per-use |
| **Hosting** | Vercel, Railway, or Fly.io | Deploy fast, scale later. | Free tier → $20/mo |
| **Database** | Supabase or PlanetScale | Managed Postgres with auth and storage included. | Free tier → $25/mo |
| **Automation** | n8n (self-hosted) or Make | Visual workflow builder for connecting everything. | Free → $30/mo |

### Business Operations

| Category | Recommended | Why | Cost |
|----------|------------|-----|------|
| **Task Management** | OmniFocus, Linear, or Todoist | Track what needs to happen. Pick one, not three. | $0-15/mo |
| **Notes / Knowledge Base** | Obsidian (local) | Your second brain. Strategies, decisions, learnings. | Free |
| **Email** | Google Workspace | Professional email + Calendar + Drive. | $7/mo |
| **CRM** | Spreadsheet → Folk or Attio | Start with a spreadsheet. Graduate when you have 50+ contacts. | Free → $20/mo |
| **Calendar** | Google Calendar | Scheduling, time blocking, client calls. | Included |

### Content & Marketing

| Category | Recommended | Why | Cost |
|----------|------------|-----|------|
| **Website** | Next.js on Vercel, or Framer | Fast, professional, easy to update. | Free → $15/mo |
| **Video** | OBS + DaVinci Resolve | Record and edit without subscriptions. | Free |
| **Design** | Figma or Canva | Thumbnails, social graphics, presentations. | Free tier |
| **Social Scheduling** | Buffer or native posting | Don't overcomplicate this. | Free → $15/mo |
| **Analytics** | Plausible or PostHog | Privacy-respecting, simple analytics. | Free tier |

### AI Agent Infrastructure

| Category | Recommended | Why | Cost |
|----------|------------|-----|------|
| **Agent Framework** | Claude Code + MCP Servers | Native tool use, extensible via MCP protocol. | Included w/ Claude |
| **Vector Database** | Supabase pgvector or Pinecone | For RAG and knowledge retrieval. | Free tier |
| **Monitoring** | Custom dashboard or Langfuse | Track agent performance, costs, errors. | Free tier |
| **Prompt Management** | Version-controlled markdown files | Keep prompts in Git. Version them. Review changes. | Free |

## The "Start Here" Stack

If you're overwhelmed, start with just these:

1. **Claude Code** — Your AI coding partner.
2. **Supabase** — Database, auth, and storage.
3. **n8n** — Automation workflows.
4. **Obsidian** — Notes and knowledge.
5. **Google Workspace** — Email and calendar.

Total cost: ~$27/month. Everything else can wait until you need it.

## Running the Prompt

```bash
# Copy-paste the prompt from:
cat prompts/tech-stack-prompt.md
```

The prompt will help you customize this stack based on your specific niche and technical background.

---

**Previous ←** [Ideal Customer](../01-validate/ideal-customer.md)
**Next →** [Automation Playbooks](automation-playbooks.md)
