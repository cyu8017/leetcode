// LeetCode 1958 - Check if Move is Legal
// https://leetcode.com/problems/check-if-move-is-legal/

func checkMove(board [][]byte, rMove int, cMove int, color byte) bool {
	opp := byte('W')
	if color == 'W' {
		opp = 'B'
	}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}}
	for _, d := range dirs {
		r, c := rMove+d[0], cMove+d[1]
		steps := 0
		for r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] == opp {
			r += d[0]
			c += d[1]
			steps++
		}
		if steps > 0 && r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] == color {
			return true
		}
	}
	return false
}
