// LeetCode 0419 - Battleships in a Board
// https://leetcode.com/problems/battleships-in-a-board/

func countBattleships(board [][]byte) int {
	count := 0
	rows := len(board)
	cols := len(board[0])

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if board[row][col] != 'X' {
				continue
			}
			if row > 0 && board[row-1][col] == 'X' {
				continue
			}
			if col > 0 && board[row][col-1] == 'X' {
				continue
			}
			count++
		}
	}

	return count
}
