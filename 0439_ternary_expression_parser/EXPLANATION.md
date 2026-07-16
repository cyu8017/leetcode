# How We Solve Ternary Expression Parser

Find the top-level colon that matches the first question mark, then recurse.

## Steps

1. If there is no `?`, return the single character.
2. Scan for the matching `:` with nesting depth for nested ternaries.
3. Recurse on the true branch if the condition is `T`, otherwise the false branch.
