# How We Solve Search a 2D Matrix II

Start at the top-right corner and eliminate a row or column each step.

## Steps

1. Begin at row 0 and the last column.
2. If the current value equals the target, return true.
3. If it is larger than the target, move left.
4. If it is smaller, move down.
5. Return false if the search walks off the matrix.
