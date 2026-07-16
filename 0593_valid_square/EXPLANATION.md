# How We Solve Valid Square

Compare the six pairwise squared distances among the four points.

## Steps

1. Compute all six distances and sort them.
2. Require four equal positive side lengths.
3. Require two equal diagonals that satisfy `diag^2 == 2 * side^2`.
