# How We Solve Valid Tic-Tac-Toe State

Enforce turn counts and that only the player who just moved can have won.

## Steps

1. Require `o_count` in `{x_count, x_count-1}`.
2. Detect wins on rows/cols/diagonals.
3. Reject dual wins or a win with the wrong turn count.
