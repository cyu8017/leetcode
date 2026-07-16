// LeetCode 0289 - Game of Life
// https://leetcode.com/problems/game-of-life/

func gameOfLife(board [][]int) {
	rows, cols := len(board), len(board[0])

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			liveNeighbors := 0
			for dr := -1; dr <= 1; dr++ {
				for dc := -1; dc <= 1; dc++ {
					if dr == 0 && dc == 0 {
						continue
					}
					nextRow := row + dr
					nextCol := col + dc
					if nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols &&
						board[nextRow][nextCol]&1 == 1 {
						liveNeighbors++
					}
				}
			}
			if board[row][col]&1 == 1 && (liveNeighbors == 2 || liveNeighbors == 3) {
				board[row][col] |= 2
			} else if board[row][col]&1 == 0 && liveNeighbors == 3 {
				board[row][col] |= 2
			}
		}
	}

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			board[row][col] >>= 1
		}
	}
}
