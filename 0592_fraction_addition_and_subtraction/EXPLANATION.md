# How We Solve Fraction Addition and Subtraction

Parse each signed numerator/denominator and accumulate with a running sum.

## Steps

1. Extract all signed integers from the expression in pairs.
2. Add each fraction onto the running numerator/denominator.
3. Reduce by gcd after each step and format as `num/den`.
