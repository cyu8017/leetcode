# How We Solve Expression Add Operators

Backtrack over split points while tracking running value and last term for multiplication.

## Steps

1. Try every substring starting at each index (respect leading-zero rules).
2. On the first number, seed path, value, and previous term.
3. Recurse with plus, minus, or multiply branches.
4. For multiply, undo the previous term before applying the product.
5. Record paths whose final value equals the target.
