# How We Solve Median Employee Salary

Rank salaries within each company and keep the middle one or two rows.

## Steps

1. Partition by company and order by salary, then id.
2. Compute each company's employee count.
3. Keep rows whose rank is the lower or upper median index.
