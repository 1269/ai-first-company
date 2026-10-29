# AI Tool Landscape

A practical guide to the current AI tools that matter for building an AI-first company. Updated regularly. Not comprehensive — intentionally opinionated.

## AI Coding Assistants

Your primary development tool. Pick one and go deep.

| Tool | Best For | Price |
|------|----------|-------|
| **Claude Code** | Terminal-based agentic coding. Deep context, file editing, multi-step tasks. | $20/mo (Pro) or API usage |
| **Cursor** | IDE-based coding with AI. Best for people who want VS Code + AI. | $20/mo |
| **Windsurf** | Similar to Cursor. Good alternative. | $15/mo |
| **GitHub Copilot** | Inline code completion. Best as a complement, not primary tool. | $10-19/mo |

**Recommendation:** Claude Code if you're comfortable in the terminal. Cursor if you want a GUI. Use this repo's `.claude/commands/` or `.cursor/rules/` depending on your choice.

## AI APIs

For building agents and automations that run on your behalf.

| Provider | Best Model | Best For |
|----------|-----------|----------|
| **Anthropic (Claude)** | Claude Sonnet / Opus | Complex reasoning, long context, tool use, coding |
| **OpenAI** | GPT-4o / o1 | General purpose, broad integrations |
| **Google (Gemini)** | Gemini Pro | Long context, multimodal |
| **Open Source** | Llama, Mistral, Qwen | Self-hosted, privacy-sensitive, cost optimization |

**Recommendation:** Start with Claude or OpenAI. Use whichever has better tool integration for your use case. You can always swap later — abstract your AI calls behind a simple interface.

## Automation Platforms

For connecting tools and building workflows without writing code for every integration.

| Tool | Best For | Price |
|------|----------|-------|
| **n8n** | Self-hosted, full control, AI-native nodes, complex workflows | Free (self-hosted) or $20/mo (cloud) |
| **Make (Integromat)** | Visual workflows, wide integration library | Free tier → $9/mo |
| **Zapier** | Simplest automation, huge app library, less flexibility | Free tier → $20/mo |

**Recommendation:** n8n if you're technical and want full control. Make if you want visual simplicity. Zapier only for simple 2-step automations.

## Agent Frameworks

For building AI agents that use tools, reason about tasks, and take actions.

| Framework | Best For | Maturity |
|-----------|----------|----------|
| **Claude Code + MCP** | Tool-using agents with Model Context Protocol servers | Production-ready |
| **LangChain / LangGraph** | Complex agent chains, state machines | Mature but complex |
| **CrewAI** | Multi-agent collaboration | Growing |
| **Custom (API + tools)** | Full control, simple agents | Always works |

**Recommendation:** Start simple. A single Claude API call with tools defined is an "agent." Don't adopt a framework until you've outgrown direct API calls.

## Vector Databases

For RAG (Retrieval-Augmented Generation) — giving your agents access to your knowledge base.

| Tool | Best For | Price |
|------|----------|-------|
| **Supabase pgvector** | Already using Supabase? Use this. | Included |
| **Pinecone** | Managed, scalable, easy to use | Free tier → $70/mo |
| **Chroma** | Local-first, open source | Free |

**Recommendation:** Supabase pgvector if you're on Supabase. Pinecone if you want managed simplicity. Don't over-invest here early — a well-prompted AI with web search often beats RAG for small knowledge bases.

## The "Don't Overcomplicate It" Rule

For your first 12-week sprint, you need:

1. An AI coding assistant (Claude Code or Cursor).
2. An AI API key (Anthropic or OpenAI).
3. A way to automate (n8n or Make).
4. A place to store data (Supabase or a spreadsheet).
5. A way to communicate (email + calendar).

Everything else is optimization. Optimize after you have revenue.

---

*Last updated: 2026. The AI tool landscape changes fast. When in doubt, search for recent comparisons.*
