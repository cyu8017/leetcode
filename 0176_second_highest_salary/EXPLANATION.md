# How We Solve Second Highest Salary

Pick the second distinct salary with an ordered offset query.

## Steps

1. Select distinct salaries from `Employee`.
2. Order them descending.
3. Skip the first row with `OFFSET 1`.
4. Take one row as `SecondHighestSalary`.
5. If none remains, the scalar subquery returns null.
