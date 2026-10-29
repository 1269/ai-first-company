# Automation Playbooks

**Phase 2: Build → Step 2**

An AI-first company doesn't hire for tasks that AI can handle. This guide covers the core automations every solo AI-first operator should have running from day one.

## The Automation Hierarchy

Not everything should be automated. Use this hierarchy:

```
Level 1: Eliminate     →  Stop doing it entirely. Does it even matter?
Level 2: Automate      →  AI/workflow handles it end-to-end, no human touch.
Level 3: Semi-automate →  AI does 80%, you review and approve.
Level 4: Assist        →  You do the work, AI speeds you up.
Level 5: Manual        →  High-judgment, high-stakes, or one-time tasks.
```

Start at Level 1. Most people skip straight to automation and end up automating things they should have eliminated.

## Core Playbooks

### 1. Lead Capture & Response

**Trigger:** Someone fills out your contact form or sends an inquiry email.
**Automation:**
- Capture lead info into your CRM/spreadsheet.
- AI drafts a personalized response based on their inquiry.
- Auto-schedule a discovery call (Calendly/Cal.com link).
- Notify you via Slack/email with context summary.

**Tools:** n8n or Make + your email provider + calendar.

### 2. Content Repurposing Engine

**Trigger:** You publish a long-form piece (video, blog post, newsletter).
**Automation:**
- Extract key points and quotes.
- AI generates 3-5 social media posts (LinkedIn, X/Twitter).
- AI creates a short-form summary for newsletter.
- Queue posts in your scheduling tool.
- You review and approve before publishing.

**Tools:** n8n + AI API + Buffer/scheduling tool.

### 3. Client Onboarding

**Trigger:** Client signs contract / pays invoice.
**Automation:**
- Create project folder (Google Drive / Notion).
- Send welcome email with next steps.
- Create tasks/milestones in project tracker.
- Schedule kickoff call.
- Add to client communication channel.

**Tools:** n8n + Google Workspace + project management tool.

### 4. Weekly Metrics Dashboard

**Trigger:** Every Monday morning (scheduled).
**Automation:**
- Pull key metrics (revenue, leads, content views, agent performance).
- AI generates a summary with insights and recommendations.
- Deliver to your inbox or Slack.

**Tools:** n8n + data sources + AI API.

### 5. Invoice & Follow-Up

**Trigger:** Project milestone completed or recurring billing date.
**Automation:**
- Generate invoice from template.
- Send to client.
- Track payment status.
- Auto-send follow-up at 7, 14, 30 days if unpaid.

**Tools:** Stripe/invoicing tool + n8n.

## Building Your First Automation

Don't build all 5 at once. Start with whichever one you're currently doing manually the most.

For each automation:

1. **Document the manual process** — Write out every step you currently do by hand.
2. **Identify the trigger** — What event starts the process?
3. **Map the workflow** — Draw the flow: trigger → step 1 → step 2 → output.
4. **Build in n8n/Make** — Start simple. Get it working. Then refine.
5. **Add AI where it helps** — Not everything needs AI. Use it where judgment, language, or personalization is required.

## Running the Prompt

```bash
# Copy-paste the prompt from:
cat prompts/automation-playbook-prompt.md
```

---

**Previous ←** [Tech Stack](tech-stack.md)
**Next →** [Phase 3: Content Engine](../03-launch/content-engine.md)
