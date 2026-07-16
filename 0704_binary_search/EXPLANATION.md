# How We Solve Binary Search

Classic left/right mid check on a sorted array.

## Steps

1. While the window is non-empty, compare `nums[mid]` to `target`.
2. Move left or right half accordingly.
3. Return the index or `-1`.
