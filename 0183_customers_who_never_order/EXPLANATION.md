# How We Solve Customers Who Never Order

Find customers whose ids never appear in `Orders`.

## Steps

1. Select customer names from `Customers`.
2. Exclude ids present in `Orders.customerId`.
3. Use `NOT IN` or an anti-join.
4. Alias the name column as `Customers`.
5. Return the remaining customers.
