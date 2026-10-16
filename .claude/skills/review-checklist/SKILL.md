---
name: review-checklist
description: Reviews a product brief against the student's own four-point checklist before it goes any further — does it name who owns it, say how we'll know it worked, keep the same scope from start to end, and explain the problem before proposing a fix. Use it when the student says "review-checklist", "review this brief", "check this brief", "run my checklist on …", or points at a brief (a file path, a wiki page, or pasted text) and asks if it's ready. Reports only; never edits the brief.
---

# Review checklist

The student wants the same four checks run on any brief, every time, without
explaining them again. Run exactly these four, in this order, and nothing else.
Don't add your own criteria, a score, or general writing feedback.

## 1. Get the brief

- **A file path** (`.md`, `.txt`, `.html`): read it. For `.html`, judge the
  visible text, not the markup.
- **A `.docx`**: extract the text first (`textutil -convert txt -stdout <file>` on
  a Mac).
- **A wiki page** (a rook-wiki title, id or link): read it with the rook-wiki
  `read_page` tool. Judge the page body; the comments under it are context, not
  part of the brief.
- **Pasted text**: use it as given.
- **Nothing given**: if a brief was written or discussed earlier in this
  session, use that one and say which file. Otherwise ask one short question:
  "Which brief should I check?"

Read the whole brief before judging any check.

## 2. Run the four checks

Give each one a verdict: **Pass**, **Partly**, or **Missing**.

1. **Names who owns it.** Pass: a named person or team is responsible for
   delivering it, not just a list of people consulted. Partly: owners are named
   for pieces but nobody owns the whole, or the owner is a role with no name
   ("the eng team") where a name was clearly available. Missing: no owner.
2. **Says how we'll know it worked.** Pass: at least one measure, with a
   direction or target, plus when or where it will be checked (for example:
   "acceptance rate back above 75% within four weeks, in Ravi's weekly report").
   Partly: metrics are named but with no target, or "we'll monitor X" with no
   bar for success. Missing: no way to tell whether it worked.
3. **The scope at the end matches the scope at the start.** Compare what the
   brief promises early (problem, proposal, scope, "what changes") with what it
   commits to late (next steps, owners, asks, timeline). Pass: the same things.
   Partly: small drift, such as one item added or dropped quietly. Missing: the
   end commits to something meaningfully bigger, smaller or different from the
   start. A section that explicitly says it's out of scope doesn't count as
   drift; scope that grows without saying so does.
4. **Explains the problem before it proposes a fix.** Pass: the problem, and
   who it hurts, comes before any solution. Partly: the problem is there but
   thin, or it shows up after the fix is already pitched. Missing: it opens
   with the fix, or never states the problem.

For every verdict, quote the brief's own words as evidence: a short phrase,
with its section heading or line number. For Partly or Missing, also give one
plain sentence on what would make it pass. Don't rewrite the brief for them.

## 3. Report

Use this layout every time, so reviews are easy to compare:

```
Review: <brief title> (<file or source>)

✓ / ~ / ✗  Names who owns it: <Pass/Partly/Missing>
   Evidence: "<quote>" (<section or line>)
   To pass: <one sentence, only if not Pass>

✓ / ~ / ✗  Says how we'll know it worked: …
✓ / ~ / ✗  Scope at the end matches the start: …
✓ / ~ / ✗  Problem before the fix: …

Ready to go further: Yes / Not yet (<n> of 4 to fix)
```

✓ is Pass, ~ is Partly and ✗ is Missing. "Ready to go further" is Yes only when
all four pass.

## Rules

- Report only. Never edit, reformat or save over the brief, even when a fix is
  obvious. If the student then asks for changes, that's a separate request.
- Judge what's written, not what you know from elsewhere. If the session knows
  the owner but the brief doesn't say, the check fails.
- Keep it short. No summary of the brief, no extra findings, no praise padding.
