# How We Solve Max Sum of Rectangle No Larger Than K

Compress rows and use sorted prefix sums to cap subarray sums at k.

## Steps

1. Fix top and bottom rows, accumulating column sums.
2. Track running prefix sums in sorted order.
3. Use lower_bound to find the best prior prefix within the k limit.
