# How We Solve Generate Parentheses

Make all valid bracket strings with n pairs, like n=3 -> "((()))", etc.

## Steps

1. Start with an empty string and open=0, close=0.
2. If open < n, you may add "(".
3. If close < open, you may add ")".
4. When length is 2*n, save the string.
5. Backtrack: try choices, then undo and try others.
6. Return all saved strings.
