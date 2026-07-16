# How We Solve Maximum Gap

Bucket sort guarantees the maximum adjacent gap after sorting.

## Steps

1. Return 0 for fewer than two numbers.
2. Place values into buckets sized by the pigeonhole principle.
3. Track each bucket's minimum and maximum.
4. The answer is the largest gap between consecutive non-empty buckets.
5. Return that gap.
