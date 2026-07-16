# How We Solve Sudoku Solver

Fill a Sudoku board so every row, column, and box has 1-9 once.

## Steps

1. Record which digits are already used in each row, column, and box.
2. Make a list of empty cells.
3. Try digits 1-9 in the next empty cell.
4. If a digit is allowed, place it and go to the next empty cell.
5. If stuck, undo (backtrack) and try another digit.
6. When all cells filled, the puzzle is solved.
