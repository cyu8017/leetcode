// LeetCode 0999 - Available Captures for Rook
// https://leetcode.com/problems/available-captures-for-rook/

func numRookCaptures(board [][]byte) int {
	m := len(board)
	r, c := -1, -1
	for i := 0; i < m; i++ {
		for j := 0; j < len(board[i]); j++ {
			if board[i][j] == 'R' {
				r, c = i, j
			}
		}
	}
	if r < 0 {
		return 0
	}
	ans := 0
	for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
		i, j := r+d[0], c+d[1]
		for i >= 0 && i < m && j >= 0 && j < len(board[i]) {
			if board[i][j] == 'B' {
				break
			}
			if board[i][j] == 'p' {
				ans++
				break
			}
			i += d[0]
			j += d[1]
		}
	}
	return ans
}
