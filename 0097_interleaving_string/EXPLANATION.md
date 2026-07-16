# How We Solve Interleaving String

Check if s3 is made by merging s1 and s2 in order.

## Steps

1. Lengths must add up; otherwise return false.
2. Use a one-row DP over s2 prefixes.
3. Mark whether the current prefixes of s1 and s2 form the matching prefix of s3.
4. A cell is true if the next letter comes from s1 or from s2 legally.
5. Return the final DP value.
