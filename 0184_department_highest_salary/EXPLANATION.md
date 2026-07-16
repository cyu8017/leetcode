# How We Solve Department Highest Salary

Join employees to departments and keep only each department's max salary.

## Steps

1. Join `Employee` to `Department` on department id.
2. For each employee, compare salary to the department maximum.
3. Keep rows equal to that maximum.
4. Select department name, employee name, and salary.
5. Return all top earners, including ties.
