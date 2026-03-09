# AI-First Project Structure

A starter scaffold for AI-first projects. Copy this structure when starting a new prototype or MVP.

```
my-project/
├── README.md              # What this project is and how to run it
├── CONTEXT.md             # AI context for this project (from your AI System)
├── docs/
│   ├── problem.md         # The problem you're solving (1 paragraph)
│   ├── scope.md           # What's in and what's out
│   └── decisions.md       # Key decisions and why you made them
├── src/                   # Your application code
└── scripts/               # Utility scripts (deploy, seed data, etc.)
```

## How to Use

1. Copy this folder structure into a new directory
2. Fill in `docs/problem.md` with your one-paragraph problem definition
3. Fill in `docs/scope.md` with your 3-feature maximum prototype scope
4. Start building in `src/`

## Why This Structure

- **CONTEXT.md** at the root means any AI tool can load project context immediately
- **docs/** captures decisions so you don't forget why you built things a certain way
- **Separation of concerns** — code in `src/`, documentation in `docs/`, scripts in `scripts/`
- **Minimal** — no over-engineering, add what you need as you need it
