# How We Solve Zuma Game

DFS with memo tries each useful insertion, then repeatedly removes runs of three or more.

## Steps

1. After each insert, shrink the board by deleting consecutive triples.
2. Only insert a hand color next to the same color on the board.
3. Memoize on `(board, hand)` and return minimum steps or −1.
