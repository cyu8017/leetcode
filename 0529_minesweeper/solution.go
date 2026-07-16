// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

func updateBoard(board [][]byte, click []int) [][]byte {
	rows := len(board)
	cols := len(board[0])
	row, col := click[0], click[1]
	directions := [8][2]int{
		{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1},
	}

	if board[row][col] == 'M' {
		board[row][col] = 'X'
		return board
	}

	var countMines func(r, c int) int
	countMines = func(r, c int) int {
		total := 0
		for _, direction := range directions {
			nr, nc := r+direction[0], c+direction[1]
			if nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] == 'M' {
				total++
			}
		}
		return total
	}

	var reveal func(r, c int)
	reveal = func(r, c int) {
		if r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != 'E' {
			return
		}
		mines := countMines(r, c)
		if mines == 0 {
			board[r][c] = 'B'
			for _, direction := range directions {
				reveal(r+direction[0], c+direction[1])
			}
		} else {
			board[r][c] = byte('0' + mines)
		}
	}

	reveal(row, col)
	return board
}
