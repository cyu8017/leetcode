# How We Solve Search Insert Position

Find where to insert target in a sorted array (or existing index).

## Steps

1. Binary search with left=0, right=n.
2. Look at middle.
3. If nums[mid] < target, search right half (left = mid+1).
4. Else search left half (right = mid).
5. When done, left is the insert position.
6. Return left.
