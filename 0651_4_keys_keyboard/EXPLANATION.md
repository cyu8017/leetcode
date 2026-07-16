# How We Solve 4 Keys Keyboard

DP over keystrokes: after `j` presses of content, Ctrl-A + Ctrl-C, then paste repeatedly.

## Steps

1. `dp[i]` = max characters after `i` keystrokes (initially just typing A).
2. For each `i`, try starting a select-copy at press `j`, then paste `i - j - 2` times → `dp[j] * (i - j - 1)`.
3. Return `dp[n]`.
