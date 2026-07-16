# How We Solve Bulb Switcher II

Only the first three bulbs matter; enumerate reachable states by press count.

## Steps

1. Cap `n` at 3 (later bulbs mirror earlier patterns).
2. For 0 / 1 / 2 / ≥3 presses, return the known distinct-state counts.
3. Lookup by `(n, presses)` from the closed-form table.
