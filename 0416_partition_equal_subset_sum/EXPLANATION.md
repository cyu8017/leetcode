# How We Solve Partition Equal Subset Sum

Subset-sum DP checks whether half the total is reachable.

## Steps

1. Reject odd totals immediately.
2. Build reachable sums with each number.
3. Return true when the half-sum target becomes reachable.
