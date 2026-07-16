# How We Solve Distribute Candies

Alice can eat at most `n / 2` candies, so the answer is limited by unique types too.

## Steps

1. Count distinct candy types.
2. Cap that count by `n / 2`.
3. Return the minimum of the two.
