# How We Solve Integer Break

Greedy decomposition into threes maximizes the product.

## Steps

1. Handle n <= 3 directly.
2. While n > 4, multiply by 3 and subtract 3.
3. Multiply the remaining n into the result.
