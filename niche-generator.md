# Niche Generator

**Phase 0: Discover → Step 3**

You've audited your skills and mapped market pain. Now it's time to commit to a niche.

This is the hardest step for most people because choosing a niche feels like closing doors. It's not. It's opening the one door that leads somewhere.

## The Niche Statement Formula

A good niche statement follows this pattern:

> **I help [specific audience] [achieve specific outcome] using AI [specific method/approach].**

Bad: "I help businesses with AI."
Good: "I help B2B SaaS companies automate their lead qualification process using AI agents, so their sales team only talks to buyers who are ready to close."

### The Three Tests

Your niche passes if you can answer YES to all three:

1. **Can you find 100 of these people in 30 minutes?** — If you can't find them, you can't sell to them.
2. **Would they take a call with you this week?** — If the pain isn't urgent, they won't buy.
3. **Can AI genuinely solve this 10x better than the status quo?** — If not, you're just a consultant with ChatGPT.

## Running the Prompt

The niche generator prompt takes your Skills Audit and Market Fit outputs and pressure-tests them into a final niche selection.

```bash
# Claude Code
/discover-niche

# Or copy-paste the prompt from:
cat prompts/niche-generator-prompt.md
```

## Committing to a Niche

Once you've selected your niche, create a `MY_NICHE.md` file in the root of this repo:

```bash
cp templates/MY_NICHE_TEMPLATE.md MY_NICHE.md
```

This file becomes your reference point for every decision going forward. When you're tempted by a shiny object, check it against your niche statement.

## What If I'm Wrong?

You probably are, a little. That's fine.

The goal isn't to pick the perfect niche on day one. The goal is to pick a *good enough* niche, validate it with real conversations and real money, and refine from there. You can pivot your niche in week 4. You can't pivot a niche you never chose.

The 12-Week Year framework (see `guides/12-week-year.md`) gives you a natural checkpoint to evaluate and adjust.

---

**Previous ←** [Market Fit](market-fit.md)
**Next →** [Phase 1: Offer Design](../01-validate/offer-design.md)
