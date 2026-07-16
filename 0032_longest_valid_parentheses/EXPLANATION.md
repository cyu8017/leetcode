# How We Solve Longest Valid Parentheses

Find the longest valid () substring.

## Steps

1. Use a stack of indexes; push -1 as a starter fence.
2. For "(", push its index.
3. For ")", pop a match; if stack empty, push current index as new fence.
4. Else length = i - stack top; keep the best length.
5. Return the best length.
