# How We Solve Remove Invalid Parentheses

Breadth-first search removes parentheses level by level until valid strings appear.

## Steps

1. BFS over strings with one parenthesis removed per step.
2. Check validity with a running balance count.
3. Stop expanding deeper once any valid string is found at the current level.
4. Collect all valid strings from that level.
