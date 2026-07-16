# How We Solve Knight Probability in Chessboard

DP the probability mass on each square after each move.

## Steps

1. Start with probability 1 at `(row, column)`.
2. Each step spreads `1/8` to the eight knight targets that stay on the board.
3. Sum remaining probability after `k` moves.
