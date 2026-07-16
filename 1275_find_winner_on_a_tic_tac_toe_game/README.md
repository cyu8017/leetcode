# 1275. Find Winner on a Tic Tac Toe Game

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)
- **Tags:** array, hash-table, matrix, simulation

## Problem

**Tic-tac-toe** is played by two players `A` and `B` on a `3 x 3` grid. The rules of Tic-Tac-Toe are:

- Players take turns placing characters into empty squares `' '`.

	- The first player `A` always places `'X'` characters, while the second player `B` always places `'O'` characters.

	- `'X'` and `'O'` characters are always placed into empty squares, never on filled ones.

	- The game ends when there are **three** of the same (non-empty) character filling any row, column, or diagonal.

	- The game also ends if all squares are non-empty.

	- No more moves can be played if the game is over.

Given a 2D integer array `moves` where `moves[i] = [row_{i}, col_{i}]` indicates that the `i^{th}` move will be played on `grid[row_{i}][col_{i}]`. return *the winner of the game if it exists* (`A` or `B`). In case the game ends in a draw return `"Draw"`. If there are still movements to play return `"Pending"`.

You can assume that `moves` is valid (i.e., it follows the rules of **Tic-Tac-Toe**), the grid is initially empty, and `A` will play first.

**Example 1:**

```
**Input:** moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
**Output:** "A"
**Explanation:** A wins, they always play first.
```

**Example 2:**

```
**Input:** moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
**Output:** "B"
**Explanation:** B wins.
```

**Example 3:**

```
**Input:** moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
**Output:** "Draw"
**Explanation:** The game ends in a draw since there are no moves to make.
```

**Constraints:**

- `1 <= moves.length <= 9`

	- `moves[i].length == 2`

	- `0 <= row_{i}, col_{i} <= 2`

	- There are no repeated elements on `moves`.

	- `moves` follow the rules of tic tac toe.

### Hints

1. It's straightforward to check if A or B won or not, check for each row/column/diag if all the three are the same.
2. Then if no one wins, the game is a draw iff the board is full, i.e. moves.length = 9 otherwise is pending.

## Approach

<!-- Describe your solution approach here -->
