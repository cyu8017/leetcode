# How We Solve Paint House

Dynamic programming keeps the minimum cost for each color at every house.

## Steps

1. Initialize the first row costs for red, green, and blue.
2. For each next house, compute the cheapest way to paint each color.
3. Each color cost adds the current paint cost plus the best previous non-matching color.
4. Slide the DP row forward house by house.
5. Return the minimum of the final three costs.
