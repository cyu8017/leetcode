# How We Solve Paint House II

For each house, track the cheapest and second-cheapest previous colors.

## Steps

1. Initialize costs for the first house.
2. For each later house, find the minimum and second minimum previous costs.
3. Paint each color with the best non-conflicting previous cost.
4. Slide the DP row forward.
5. Return the minimum cost in the final row.
