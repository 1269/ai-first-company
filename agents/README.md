# AI Agents

This directory contains agent templates and real-world examples for AI-first businesses.

## Structure

```
agents/
├── templates/     # Starter agent configs — fork and customize
└── examples/      # Real-world agents from the community
```

## What's an Agent?

In this framework, an "agent" is any AI-powered automation that:
- Has a clear, specific purpose.
- Is triggered by an event, schedule, or human action.
- Takes inputs, processes them with AI, and produces outputs.
- Has guardrails defining what it should never do.
- Has human checkpoints where appropriate.

## Creating a New Agent

Use the Claude Code command:

```bash
/generate-agent
```

Or manually create a folder in `templates/` with:

```
agents/templates/[agent-name]/
├── README.md          # What it does, how to deploy
├── system-prompt.md   # The agent's system prompt
└── config.json        # Triggers, inputs, outputs, guardrails
```

## Agent Template: config.json

```json
{
  "name": "Agent Name",
  "description": "One sentence description.",
  "version": "0.1.0",
  "trigger": {
    "type": "manual | schedule | event | webhook",
    "details": "Description of what starts the agent."
  },
  "inputs": [
    {
      "name": "input_name",
      "type": "string | object | array",
      "source": "Where this data comes from",
      "required": true
    }
  ],
  "outputs": [
    {
      "name": "output_name",
      "type": "string | object | array",
      "destination": "Where the output goes"
    }
  ],
  "guardrails": [
    "What the agent must NEVER do"
  ],
  "human_checkpoints": [
    "Where a human reviews before the agent continues"
  ],
  "tools": [
    {
      "name": "tool_name",
      "purpose": "What it's used for"
    }
  ]
}
```

## Contributing Agents

Built an agent for your AI-first business? Share it:

1. Create a folder in `examples/` with your agent name.
2. Include README.md, system-prompt.md, and config.json.
3. Document what niche/industry it's for and what problem it solves.
4. Submit a PR. See [CONTRIBUTING.md](../CONTRIBUTING.md).
