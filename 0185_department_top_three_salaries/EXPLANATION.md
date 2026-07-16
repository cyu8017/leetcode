# How We Solve Department Top Three Salaries

Dense-rank salaries within each department and keep ranks 1-3.

## Steps

1. Partition employees by department and rank salaries descending.
2. Use `DENSE_RANK` so ties share a rank.
3. Join the ranked rows to `Department`.
4. Keep rows with rank at most 3.
5. Return department, employee, and salary.
