# How We Solve Fraction to Recurring Decimal

Long division with a remainder map detects the repeating cycle.

## Steps

1. Handle zero and the overall sign first.
2. Emit the integer quotient.
3. While a remainder remains, record its position in the decimal.
4. Multiply by 10, append the next digit, and update the remainder.
5. When a remainder repeats, wrap that span in parentheses.
