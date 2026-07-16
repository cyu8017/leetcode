# How We Solve Managers with at Least 5 Direct Reports

Count reports per manager id, then return managers with count ≥ 5.

## Steps

1. Group employees by `managerId`.
2. Keep manager ids with at least five direct reports.
3. Select those managers' names from `Employee`.
