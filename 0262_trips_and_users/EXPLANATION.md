# How We Solve Trips and Users

Compute daily cancellation rates for unbanned clients over a date range.

## Steps

1. Join trips with users on client id where the user role is client.
2. Keep only unbanned clients and dates in the target range.
3. Group by request date.
4. Divide non-completed trips by total trips and round to two decimals.
5. Order the results by day.
