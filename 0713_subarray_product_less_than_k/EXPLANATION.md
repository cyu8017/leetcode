# How We Solve Subarray Product Less Than K

Sliding window: keep the product of `nums[left..right]` strictly below `k`.

## Steps

1. Expand `right`, multiplying into the product.
2. Shrink `left` while the product is `>= k`.
3. Add `right - left + 1` valid subarrays ending at `right`.
