# Marketing Department: Onboarding

The marketing department for [YOUR BUSINESS NAME]: how the business gets found and turns attention into customers. Read `marketing.md` for what it is for, who does what, and what needs the owner's yes. It is the source of truth.

## Where things go

| Path | Holds |
|------|-------|
| `marketing.md` | What the department is for, its boundary, its offers, who does what, gated actions, review cadence. |
| `tasks/` | Task documents: one file per job that more than one agent works on. Each holds the job, who does what, the work itself (Research, Plan, Build notes, Review) and the Session notes. |
| `task-template.md` | The blank task document. Copy it to `tasks/<job-name>.md` to start a new job. |
| `tools/close-out.py` | The close-out hook: Claude Code and Codex run it when a session stops. |

## Conventions

- **The close-out rule.** Before your session ends, write back to the task document you worked on: put your work in its section (Research, Plan, Build notes or Review), then add one dated line under Session notes saying who you are (the tool and model), what you did, and what is next. The next agent starts from that file, not from your chat. This applies to every tool that works here.
- **A rule asks, a hook makes sure.** In Claude Code and Codex, `tools/close-out.py` also writes a line under Session notes when a session stops. It records what was asked and what you said last. Write your own line anyway: only you can say what is next.
- **Stay in your step.** Change only the section your step writes to, and add your Session notes line. Don't rewrite another agent's work. If you disagree with it, say so in your own section.
- **Every claim in Research has a source link.** A quote you could not open on its own page is marked unverified.
- **Gated actions stop the agent.** Spend, publish, send, sign: stop and ask the owner in the session, and wait for a yes (see `marketing.md`).
- **Link, never copy.** The brand lives in [WHERE YOUR BRAND LIVES] and the offers' facts in [WHERE YOUR OFFER DETAILS LIVE]. Read them there and point at them. Don't retype them into this folder, where they go stale.
- **Git.** This folder is a git repository, so every change can be seen (`git diff`) and undone. Don't commit or push unless the owner asks.
