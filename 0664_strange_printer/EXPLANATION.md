# How We Solve Strange Printer

Interval DP: a turn printing `s[i]` can also cover later equal characters.

## Steps

1. `dfs(i,j)` = min turns for `s[i..j]`.
2. Base: print `s[i]` then solve `i+1..j`.
3. For each `k` with `s[k]==s[i]`, try `dfs(i,k-1)+dfs(k+1,j)`.
