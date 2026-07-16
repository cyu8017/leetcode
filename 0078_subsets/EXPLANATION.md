# How We Solve Subsets

List every subset of the given numbers.

## Steps

1. Start with the empty subset.
2. For each number, copy every existing subset and add the number.
3. Append those new subsets to the list.
4. Repeat for all numbers.
5. Return the full power set.
