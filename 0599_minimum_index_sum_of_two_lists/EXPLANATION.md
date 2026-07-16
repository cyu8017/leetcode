# How We Solve Minimum Index Sum of Two Lists

Index the first list, then scan the second for shared names with minimal `i + j`.

## Steps

1. Map each string in `list1` to its index.
2. For shared strings in `list2`, compute the index sum.
3. Keep all names that achieve the minimum sum.
