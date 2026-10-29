# Lead Research Agent

An AI agent that researches prospects and generates personalized outreach context.

## What It Does

Given a prospect's name and company, this agent:
1. Researches the person (LinkedIn activity, published content, recent posts).
2. Researches the company (recent news, funding, job postings, tech stack).
3. Identifies trigger events (expansion, new hire, funding round, product launch).
4. Generates personalized talking points for outreach.
5. Drafts a value-first outreach message.

## When to Use

- Before sending outbound outreach messages.
- Before discovery calls to prepare context.
- As part of an automated lead pipeline.

## Deployment Options

### Option A: Claude Code (Manual)
Run the system prompt as a one-off query with prospect details.

### Option B: n8n Workflow (Automated)
1. Trigger: New row added to prospect spreadsheet.
2. Web search nodes gather prospect/company data.
3. AI node processes data using the system prompt.
4. Output saved back to spreadsheet or sent to Slack.

### Option C: Custom Script
Use the Anthropic API with web search tools to run this programmatically.

## Configuration

See `config.json` for the full configuration. Key settings:

- **Trigger:** Manual (prospect name + company) or automated (new CRM entry).
- **Guardrails:** Never fabricate information. Flag low-confidence findings. Never send outreach without human review.
- **Human Checkpoint:** Draft message must be approved before sending.
