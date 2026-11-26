# Marketing Department Prompt

Builds your own marketing department: one folder that Claude Code, Codex and Antigravity all work in, where every session writes what it did back to the same task document before it ends. It's the setup from the video *Claude vs ChatGPT vs Gemini: Stop Choosing, Use All 3 on One Project*. What it builds and how it works: [templates/marketing-department](../../templates/marketing-department/).

**Run it in a terminal AI tool, not a chat app.** Make an empty folder (for example `marketing-department`), open Claude Code, Codex or Antigravity in it, and paste everything below the line. The chat apps can't write files on your computer.

It takes about ten minutes: seven short questions, then the build.

---

You're setting up my marketing department in this folder. It's one folder that every AI tool I use can work in. Every session writes what it did back to a task document before it ends, so the next model starts where the last one stopped and I never have to pick one model.

Build it from the template at https://github.com/1269/ai-first-company/tree/main/templates/marketing-department. Copy its files exactly; don't write your own versions of them.

## Step 1: Check the folder

- Work only in this folder. If it isn't empty, list what's in it and ask me before you go on. Never delete or overwrite a file that's already here.
- Check that `git` and `python3` are installed (`git --version`, `python3 --version`). If one is missing, tell me how to install it on my computer and stop.
- If your sandbox blocks any step below (the download, writing `.codex/` or `.git/`, the commit), don't work around it: ask me to approve it, or give me the exact command to run myself, then carry on.

## Step 2: Interview me

Ask these one at a time, and wait for my answer before the next one. Keep each question to a line or two, with a short example answer. If I say "skip", use the default in brackets, or "(not set yet)" where there's no default, and tell me which you used.

1. What's your business called, what does it do, and who do you sell to? One or two sentences.
2. Which offer should marketing work on first? Its name, who it's for, the one thing you want people to do (book a call, buy, sign up) with its link, and where its price and details live (a web page or a file).
3. Where does your brand live: your website, and any file or folder with your voice, colours or brand guide? [only the website, if there is one]
4. Which AI tools do you use in the terminal: Claude Code, Codex, Antigravity, others? [only the tool running this prompt]
5. What should marketing cover for you? [offer pages, email, social posts and launches]
6. Spending money, publishing, sending messages and signing anything already need your yes. Is there anything else an agent must ask you about first? [nothing else]
7. What's the first job for the department, and where should the result go? One thing, like "a landing page for the offer, in my website's code folder", "a launch email, as a Google Doc" or "five LinkedIn posts, in this folder". [a landing page for the offer from question 2; where it goes is settled in the plan]

## Step 3: Copy the template

1. Download the repo into a hidden folder here: `git clone --depth 1 https://github.com/1269/ai-first-company.git .template-download`.
2. Copy everything inside `.template-download/templates/marketing-department/` into this folder, hidden files included. Leave out its `README.md`, which describes the template, not my department.
3. Check that these are all here before you go on: `AGENTS.md`, `CLAUDE.md`, `marketing.md`, `task-template.md`, `tasks/.gitkeep`, `tools/close-out.py`, `.claude/settings.json`, `.codex/hooks.json`, `.gitignore`. Then delete `.template-download`.

## Step 4: Fill it in

- In `AGENTS.md` and `marketing.md`, replace every `[BRACKETED PLACEHOLDER]` with my answers. Use my words, and add nothing I didn't say. Where I gave no answer, write "(not set yet)".
- In "Who does what", name only the tools I have. The defaults: Gemini in Antigravity researches, every tool answers the planning question and I pick one answer, Codex builds, and a different model from the builder reviews. If I have one tool, it does every step, and the review runs in a fresh session that's told to argue with the work.
- Add the extra gated actions from my answer to question 6.
- Create the first job: copy `task-template.md` to `tasks/<job-name>.md` (lowercase words joined by dashes, like `tasks/offer-landing-page.md`). Fill in "The job" and "Who does what" from my answers, with "(not set yet)" for anything I haven't said, like how to preview it. Leave Research, Plan, Build notes and Review as "(empty)". Don't start the job.
- Check that nothing is left to fill: `grep -rnE "\[[A-Z][A-Z0-9 ,.'/:()-]+\]" AGENTS.md marketing.md tasks/` prints nothing (grep then exits 1, which is the pass). `task-template.md` keeps its placeholders on purpose.

## Step 5: Turn it on

1. Follow the close-out rule yourself: add one line under Session notes in the new task document with today's date, who you are (the tool and model), "set up the department", and "next: Research".
2. Run `git init`, then commit everything: `git add -A && git commit -m "marketing: set up the department"`. If git says it doesn't know who I am, ask me for a name and email, set them for this folder only (`git config user.name "<name>"` and `git config user.email "<email>"`, no `--global`), and commit again. Don't add a remote and don't push. Codex finds its hook through git, and git lets me see and undo what any agent changes.
3. Check the hook runs: `echo '{}' | python3 tools/close-out.py claude` exits 0, and `git status` shows nothing changed. This only proves it runs; Step 6 says how I'll see it write.

## Step 6: Tell me what's next

Reply with these four things, and keep it short:

1. The folder you built, one line per file saying what it holds.
2. What each tool needs once:
   - Claude Code: open it in this folder and trust the folder when it asks. From then on, its hook writes a session note every time a session stops.
   - Codex: run `codex` here once, and trust the folder and its hooks when it asks. Its hook then works the same way.
   - Antigravity: it has no end-of-session hook, so the close-out rule in `AGENTS.md` does the job. If a session forgets, ask it once: "Follow the close-out rule."
3. The first prompt to paste into every tool I use, with the job's file name filled in, so I can watch each one read the same project:

   > You're new to this project. Read AGENTS.md, marketing.md and tasks/<job-name>.md. Then tell me, in under 150 words: 1. What this department is for. 2. What this job is asking for. 3. The first thing you would do on it, and what you'd need from me. Don't change any files yet.

   Then how to see the hook work: after Claude Code and Codex answer it, each adds a line under Session notes in the task document, even though they changed nothing else. No line from one of them means that folder or its hooks aren't trusted yet.

4. Where the prompts for the rest of the job are: "Run your first job" in https://github.com/1269/ai-first-company/tree/main/templates/marketing-department.
