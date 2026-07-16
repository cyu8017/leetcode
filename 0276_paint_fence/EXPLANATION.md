# How We Solve Paint Fence

Dynamic programming counts valid colorings with at most two adjacent same colors.

## Steps

1. Handle n equals 1 or 2 directly with k and k squared.
2. Track totals for the previous two fence lengths.
3. Each new length multiplies the sum of the prior two by k minus 1.
4. Slide the DP window forward for n steps.
5. Return the total for length n.
