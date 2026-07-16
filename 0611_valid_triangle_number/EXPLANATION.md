# How We Solve Valid Triangle Number

Sort the sides, then for each largest side count valid pairs with two pointers.

## Steps

1. Sort `nums` ascending.
2. Fix the largest side `nums[k]` and scan `left`/`right` below it.
3. When `nums[left] + nums[right] > nums[k]`, all indices between contribute, then move `right` left.
