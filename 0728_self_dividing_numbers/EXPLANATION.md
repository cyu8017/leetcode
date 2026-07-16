# How We Solve Self Dividing Numbers

A number is self-dividing if it is divisible by every nonzero digit.

## Steps

1. For each candidate in `[left, right]`, inspect its digits.
2. Reject on a `0` digit or a failed modulus.
3. Collect the survivors.
