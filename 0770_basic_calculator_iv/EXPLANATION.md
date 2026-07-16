# How We Solve Basic Calculator IV

Parse into multivariate polynomials; substitute known variables; emit terms.

## Steps

1. Recursive-descent parse `+`, `-`, `*` and parentheses.
2. Represent polys as maps from variable tuples to coefficients.
3. Sort terms by degree then lex and format `coef*var*...`.
