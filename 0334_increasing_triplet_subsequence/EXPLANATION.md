# How We Solve Increasing Triplet Subsequence

Track the smallest first and second values seen so far.

## Steps

1. Update first when the current number is smaller.
2. Else update second when it fits between first and second.
3. Any number greater than second completes a triplet.
