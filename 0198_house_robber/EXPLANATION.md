# How We Solve House Robber

Track the best totals with and without robbing the previous house.

## Steps

1. Keep `prev2` and `prev1` as the best results for the last two houses.
2. For each house, choose max(skip it, rob it + prev2).
3. Shift the window forward.
4. Continue through the whole street.
5. Return the final best total.
