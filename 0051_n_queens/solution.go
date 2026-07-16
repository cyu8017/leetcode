// LeetCode 0051 - N-Queens
// https://leetcode.com/problems/n-queens/

import "strings"

func solveNQueens(n int) [][]string {
	result := make([][]string, 0)
	cols := make(map[int]bool)
	diag1 := make(map[int]bool)
	diag2 := make(map[int]bool)
	board := make([]string, n)
	for i := range board {
		board[i] = strings.Repeat(".", n)
	}

	var backtrack func(row int)
	backtrack = func(row int) {
		if row == n {
			copyBoard := append([]string(nil), board...)
			result = append(result, copyBoard)
			return
		}

		for col := 0; col < n; col++ {
			if cols[col] || diag1[row+col] || diag2[row-col] {
				continue
			}

			cols[col] = true
			diag1[row+col] = true
			diag2[row-col] = true

			rowChars := []byte(board[row])
			rowChars[col] = 'Q'
			board[row] = string(rowChars)

			backtrack(row + 1)

			delete(cols, col)
			delete(diag1, row+col)
			delete(diag2, row-col)
			board[row] = strings.Repeat(".", n)
		}
	}

	backtrack(0)
	return result
}
