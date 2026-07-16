# How We Solve Valid Sudoku

Check if a 9x9 Sudoku board has no repeats in rows, columns, or 3x3 boxes.

## Steps

1. Make empty sets for each row, column, and box.
2. Walk every cell.
3. Skip "." empty cells.
4. If the digit is already in its row, column, or box, return false.
5. Otherwise add the digit to those three sets.
6. If you finish with no trouble, return true.
