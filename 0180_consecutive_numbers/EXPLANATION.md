# How We Solve Consecutive Numbers

Self-join three consecutive log rows that share the same number.

## Steps

1. Alias `Logs` three times as `l1`, `l2`, and `l3`.
2. Require consecutive ids: `l1.id + 1 = l2.id` and `l2.id + 1 = l3.id`.
3. Require equal `num` across all three.
4. Select the distinct matching numbers.
5. Return them as `ConsecutiveNums`.
