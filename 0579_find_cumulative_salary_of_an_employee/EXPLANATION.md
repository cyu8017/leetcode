# How We Solve Find Cumulative Salary of an Employee

For each worked month except the latest, sum that month plus the prior two calendar months.

## Steps

1. Exclude each employee's most recent month.
2. Left-join salaries for `month - 1` and `month - 2` (missing months count as 0).
3. Order by id ascending and month descending.
