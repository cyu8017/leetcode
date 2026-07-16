# How We Solve Design Tic-Tac-Toe

Track row, column, and diagonal scores instead of the full board.

## Steps

1. Add +1 for player 1 and -1 for player 2 on each move.
2. Update row, column, and diagonal counters for the cell.
3. Return the player when any line reaches n in absolute value.
