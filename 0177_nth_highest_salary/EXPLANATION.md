# How We Solve Nth Highest Salary

A function returns the Nth distinct salary via `LIMIT`/`OFFSET`.

## Steps

1. Accept `N` as the function argument.
2. Convert it to a 0-based offset `N - 1`.
3. Select distinct salaries ordered descending.
4. Skip `N - 1` rows and take one.
5. Return null when fewer than `N` distinct salaries exist.
