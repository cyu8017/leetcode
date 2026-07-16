# How We Solve Next Greater Element I

Monotonic stack on nums2 records the next greater value for each element.

## Steps

1. Scan nums2, popping smaller stack values when a larger num appears.
2. Map each popped value to the current num.
3. Answer nums1 using that map, defaulting to −1.
