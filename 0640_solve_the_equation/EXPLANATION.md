# How We Solve Solve the Equation

Parse both sides into `coef * x + const`, then solve `coef * x = const`.

## Steps

1. Split on `=` and extract coefficients/constants with a regex tokenizer.
2. Move all terms to form `coef * x = const`.
3. Return `Infinite solutions`, `No solution`, or `x=<value>`.
