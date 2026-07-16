# How We Solve Employee Bonus

Left-join bonuses and keep employees whose bonus is missing or below 1000.

## Steps

1. Left join `Employee` to `Bonus` on `empId`.
2. Keep rows where `bonus < 1000` or `bonus` is null.
3. Return name and bonus.
