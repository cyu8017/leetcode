---
name: sync-leetcode
description: Scan LeetCode for newly published problems and scaffold missing folders in this repo. Use when the user asks to sync, check for new questions, update the problem tree, or keep folders current with LeetCode.
---

# Sync LeetCode Problems

## When to use

- User asks to check for new LeetCode questions
- User wants folders created for problems missing from the repo
- Session start hook reported new problems in `config/last-sync.json`

## Steps

1. Run sync from the repository root:

```powershell
.\scripts\sync-new-problems.ps1
```

2. Read `config/last-sync.json` for the report.

3. Tell the user:
   - How many new folders were created (if any)
   - Names of new problems
   - That the repo is up to date if `created` is 0

## Do not

- Run `scaffold-all.ps1` unless the user explicitly wants a full rebuild from cache
- Overwrite existing solution files in problem folders
- Create folders outside the `{4-digit}_{snake_case_title}` naming convention

## Source

LeetCode problem metadata is fetched from the URL in `config/sources.json` (default: daily-updated public mirror of LeetCode's problem set).
