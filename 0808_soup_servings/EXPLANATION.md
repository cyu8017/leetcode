# How We Solve Soup Servings

Scale by 25ml units and DP the four pour operations; large `n` ≈ probability 1.

## Steps

1. If `n` is huge (≥4800), return `1.0`.
2. Memoize `dp(a,b)` over the four 25ml-scaled pours.
3. Terminal: A empty first → 1, both empty → 0.5, B empty first → 0.
