# How We Solve Employees Earning More Than Their Managers

Self-join employees to their managers and compare salaries.

## Steps

1. Alias `Employee` as the worker and again as the manager.
2. Join on `worker.managerId = manager.id`.
3. Keep rows where the worker salary is greater.
4. Select the worker name as `Employee`.
5. Return those names.
