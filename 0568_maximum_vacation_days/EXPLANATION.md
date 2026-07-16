# How We Solve Maximum Vacation Days

DP over weeks and cities, allowing a stay or any available flight each Monday.

## Steps

1. Start at city `0` with zero vacation days.
2. For each week, try every reachable destination (same city or a flight).
3. Add that city's vacation for the week and keep the best ending state.
