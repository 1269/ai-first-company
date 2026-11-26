# Marketing Department

One folder that Claude, ChatGPT and Gemini all work in, so you never have to choose a model. This is the setup from the video *Claude vs ChatGPT vs Gemini: Stop Choosing, Use All 3 on One Project*: Gemini researched an offer, all three planned the page, Codex built it, Gemini reviewed it, and nothing was lost between them.

The idea in one line: the work lives in your folder, not in a chat app. Every session, whatever model runs it, writes what it did back to the same task document before it ends. The next model starts where the last one stopped, and you can swap any model out tomorrow.

## What's in the folder

```
marketing-department/
├── AGENTS.md              # Onboarding every agent reads first, with the close-out rule
├── CLAUDE.md              # Claude Code's file: one line, @AGENTS.md, so it reads the same rules
├── marketing.md           # What the department is for, its offers, who does what, what needs your yes
├── task-template.md       # The blank task document, copied for each new job
├── tasks/                 # One task document per job
├── tools/close-out.py     # The hook that writes a session note when a session stops
├── .claude/settings.json  # Runs the hook in Claude Code
├── .codex/hooks.json      # Runs the hook in Codex
└── .gitignore
```

Codex and Antigravity read `AGENTS.md` on their own. Claude Code reads `CLAUDE.md`, which points it at `AGENTS.md`. One set of rules, every tool.

## Set it up

You need a terminal AI tool that can work in a folder on your computer: [Claude Code](https://claude.com/claude-code), [Codex](https://github.com/openai/codex) (ChatGPT's) or [Antigravity](https://antigravity.google) (Google's; it replaced the Gemini CLI). Two or three is the point, but one works too. The chat apps can't write to your files.

- **Paste the prompt (the fast way).** Make an empty folder, open one of those tools in it, and paste [the marketing department prompt](../../03-launch/prompts/marketing-department-prompt.md). It asks you seven short questions, one at a time, builds the department from this template with your answers in it, and sets up your first job.
- **From this repo, in Claude Code.** Open Claude Code in your copy of this repo and type `/build-marketing-department`. It asks where to put the department.
- **By hand.** You need `git` and `python3`. Copy this folder (without this README), replace every `[BRACKETED PLACEHOLDER]` in `AGENTS.md` and `marketing.md`, copy `task-template.md` into `tasks/` for your first job and fill it in, then run `git init` and make a first commit. Codex finds the hook through git.

Then open each tool in the folder once and trust it when it asks. Codex runs a project's hooks only after you trust the folder and its hooks in an interactive `codex` session.

## How it works

### The close-out rule

It's in `AGENTS.md`, so every tool reads it:

> Before your session ends, write back to the task document you worked on: put your work in its section (Research, Plan, Build notes or Review), then add one dated line under Session notes saying who you are (the tool and model), what you did, and what is next. The next agent starts from that file, not from your chat.

Think of it as breadcrumbs. You're coordinating a few very smart coworkers, and each one leaves a note so the next one knows what's done and what's theirs to do.

### A rule asks, a hook makes sure

A model can skip a rule. So in Claude Code and Codex, `tools/close-out.py` runs every time a session stops. It reads that session's transcript and keeps one dated line per session under Session notes: the tool and model, what you asked first, and what the agent said last. It calls no model, never blocks the agent, and exits quietly on any problem.

It's a safety net, not the whole note. It records what happened; only the agent can say what's next, which is why the rule stays in `AGENTS.md` too.

Antigravity has no end-of-session hook, so there the rule does the job on its own. If a session forgets, ask it once: "Follow the close-out rule."

The hook needs `python3`. Tested on macOS with Claude Code 2.1.332 and Codex 0.172.0.

### Who does what

Starting picks, not a ranking. Change them for any job in that job's task document.

| Step | Who | Writes to |
|---|---|---|
| Research | Gemini, in Antigravity | Research |
| Plan | every tool answers the same question; you pick one answer | Plan |
| Build | Codex | Build notes |
| Review | a different model from the builder | Review |

Pick the answer, not the brand. And never let the builder review its own work: a model is a little more critical of another model's work than of its own. With only one tool, run the review in a fresh session and tell it to argue.

### Gated actions

Spend, publish, send, sign. An agent that reaches one of these stops and asks you in the session. Nothing goes public without your yes.

### Link, never copy

Your prices, offers and brand already live somewhere: your website, a brand guide. The department points at them and reads them from there, so every job starts from today's price, not a copy that went stale.

## Run your first job: the prompts from the video

Swap in your job's file name for `tasks/<job-name>.md`, and fill in the brackets.

**1. The same first prompt, in every tool.** You see how each model reads the same project, and you never had to brief any of them. The agents change nothing, but Claude Code and Codex each leave a line under Session notes: that's the hook working. No line means the folder or its hooks aren't trusted yet.

```
You're new to this project. Read AGENTS.md, marketing.md and tasks/<job-name>.md.

Then tell me, in under 150 words:
1. What this department is for.
2. What this job is asking for.
3. The first thing you would do on it, and what you'd need from me.

Don't change any files yet.
```

**2. Research, in Gemini (Antigravity).**

```
You're the researcher on tasks/<job-name>.md. Search the web and find:

1. What [THE OFFER] is and who it's for. Start at [ITS LINK].
2. Five [PAGES, EMAILS OR POSTS] selling something similar, and what each one does well: the headline, the proof, the call to action.
3. The three objections [YOUR CUSTOMER] has before buying something like this, in the words they use.

Write what you found into the task document under "## Research". Keep it short, with a source link on every claim. Don't plan and don't build anything.
```

If you research in a chat app instead (the Gemini app, ChatGPT), paste its findings into the Research section yourself.

**3. Plan: the same question, in every tool.** Answers stay in the chat, so you can compare them side by side.

```
Read the Research section of tasks/<job-name>.md.

Plan [THE JOB]. Give me:
- the headline and the subhead
- the sections in order, with one line on what each one says
- the one call to action
- what you'd reuse from what I already have so it matches ([WHERE YOUR BRAND LIVES])

Under 250 words. Answer here in the chat. Don't write to any file.
```

**4. Write down the plan you picked**, in the tool that wrote it. The agent writes exactly what you type, so put your real reason in first.

```
I'm going with your plan. Write it into tasks/<job-name>.md under "## Plan". Add one line saying every tool answered the same question and why this one was picked: [YOUR REASON].
```

**5. Build, in Codex.** It builds from the written plan, not from a fresh prompt.

```
You're the builder on tasks/<job-name>.md. Build [THE JOB] from its Plan.

It goes in [WHERE THE WORK GOES]. Read that folder's own instructions first if it has any, reuse what's already there so it matches, and take the offer's facts from [WHERE THEY LIVE]. Change nothing else.

When it's done, show me what changed, and write what you built and how you checked it under "## Build notes".
```

**6. Review, in a different model from the builder.**

```
You're the reviewer on tasks/<job-name>.md. Argue with the build: check it against the Plan and the Research, and list what's wrong or weak, worst first, each with where it is and how to fix it. Write your review under "## Review". Don't change the work itself.
```

**7. Fix, back in the builder.**

```
Read the Review in tasks/<job-name>.md and fix the top three problems. Show me what changed, and add what you fixed under "## Build notes".
```

**8. Publish.** Look at it yourself first. Then ask the tool you're driving to publish it. It stops and asks before it does, because publishing is a gated action.

Open the task document at the end. Research, the plan you picked, the build, the review and every session's note are all in one file you own.

## Let the models call each other (optional)

In the video I stop carrying work between the tools by hand with [Frenemy](https://github.com/noblehacks/frenemy), a free plugin (I'm not affiliated with it) that lets Claude Code, Codex and Gemini call each other on the subscriptions you already pay for. Whichever tool you're typing in drives: "Ask Codex to build the page from the Plan in tasks/<job-name>.md", "Get a second opinion from Gemini on the page Codex built". The prompts above work the same way with "Ask Codex to" or "Get a second opinion from Gemini on" in front. `.gitignore` already leaves out Frenemy's working copies (`.worker-state/`).

## Related

- **[psa-method](https://github.com/1269/psa-method):** the `/psa` skill that spins up projects and systems like this one in one command.
- **[AI System](https://github.com/1269/ai-system):** build your personal AI productivity system.
- **Want help setting up your own virtual departments?** [jashia.com/services](https://jashia.com/services)
