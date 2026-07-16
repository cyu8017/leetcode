# How We Solve Best Time to Buy and Sell Stock with Transaction Fee

Track best cash and best held position; selling pays the fee.

## Steps

1. `hold` = max profit while holding a share.
2. `cash` = max profit while flat.
3. Update both left-to-right; answer is final `cash`.
