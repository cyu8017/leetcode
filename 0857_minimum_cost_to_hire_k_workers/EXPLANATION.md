# How We Solve Minimum Cost to Hire K Workers

Sort by wage/quality ratio; keep the `k` lowest qualities under each ratio.

## Steps

1. Sort workers by increasing `wage/quality`.
2. Maintain a max-heap of qualities for the current group of size `k`.
3. Cost is `sum(quality) * current_ratio`; track the minimum.
