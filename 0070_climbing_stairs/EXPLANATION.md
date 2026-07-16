# How We Solve Climbing Stairs

Count ways to climb n stairs taking 1 or 2 steps at a time.

## Steps

1. One stair has 1 way; two stairs have 2 ways.
2. Keep the count for the previous two stair totals.
3. Each new total is the sum of the last two.
4. Step forward until you reach n.
5. Return that total.
