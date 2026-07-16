# How We Solve Duplicate Emails

Group by email and keep only addresses that appear more than once.

## Steps

1. Select email from `Person`.
2. Group rows by email.
3. Keep groups with `COUNT(*) > 1`.
4. Alias the column as `Email`.
5. Return the duplicate addresses.
