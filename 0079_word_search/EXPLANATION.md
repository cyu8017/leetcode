# How We Solve Word Search

Check if a word exists in a letter grid by adjacent moves.

## Steps

1. Try starting a search from every cell.
2. Use DFS to match the next letter in each direction.
3. Mark visited cells temporarily so they are not reused.
4. Backtrack and unmark if the path fails.
5. Return true if any start works.
