// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

func candyCrush(board [][]int) [][]int {
	m, n := len(board), len(board[0])
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	stable := false
	for !stable {
		stable = true
		for i := 0; i < m; i++ {
			for j := 0; j < n-2; j++ {
				value := abs(board[i][j])
				if value != 0 && value == abs(board[i][j+1]) && value == abs(board[i][j+2]) {
					board[i][j] = -value
					board[i][j+1] = -value
					board[i][j+2] = -value
					stable = false
				}
			}
		}
		for j := 0; j < n; j++ {
			for i := 0; i < m-2; i++ {
				value := abs(board[i][j])
				if value != 0 && value == abs(board[i+1][j]) && value == abs(board[i+2][j]) {
					board[i][j] = -value
					board[i+1][j] = -value
					board[i+2][j] = -value
					stable = false
				}
			}
		}
		for j := 0; j < n; j++ {
			write := m - 1
			for i := m - 1; i >= 0; i-- {
				if board[i][j] > 0 {
					board[write][j] = board[i][j]
					write--
				}
			}
			for i := write; i >= 0; i-- {
				board[i][j] = 0
			}
		}
	}
	return board
}
