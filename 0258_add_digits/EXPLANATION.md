# How We Solve Add Digits

Repeated digit sums equal the digital root formula.

## Steps

1. Return 0 immediately for input 0.
2. Otherwise compute `1 + (num - 1) % 9`.
3. This equals repeatedly summing digits until one digit remains.
4. Return that single-digit result.
