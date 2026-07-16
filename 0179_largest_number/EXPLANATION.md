# How We Solve Largest Number

Sort number strings by which concatenation is larger.

## Steps

1. Convert every integer to a string.
2. Sort so that `a` comes before `b` when `a+b` is greater than `b+a`.
3. Join the sorted strings.
4. If the result would start with zeros, return `"0"`.
5. Otherwise return the joined string.
