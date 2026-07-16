# How We Solve Minesweeper

Reveal the clicked cell, then flood-fill empty regions recursively.

## Steps

1. If a mine is clicked, mark it `X`.
2. Otherwise count adjacent mines and write the digit or `B` for zero.
3. Expand DFS when the cell has no neighboring mines.
