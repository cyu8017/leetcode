// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

func tictactoe(moves [][]int) string {
	board := [3][3]int{}
	for i, mv := range moves {
		if i%2 == 0 {
			board[mv[0]][mv[1]] = 1
		} else {
			board[mv[0]][mv[1]] = -1
		}
	}
	lines := [][3]int{}
	for r := 0; r < 3; r++ {
		lines = append(lines, [3]int{board[r][0], board[r][1], board[r][2]})
	}
	for c := 0; c < 3; c++ {
		lines = append(lines, [3]int{board[0][c], board[1][c], board[2][c]})
	}
	lines = append(lines, [3]int{board[0][0], board[1][1], board[2][2]})
	lines = append(lines, [3]int{board[0][2], board[1][1], board[2][0]})
	for _, line := range lines {
		s := line[0] + line[1] + line[2]
		if s == 3 {
			return "A"
		}
		if s == -3 {
			return "B"
		}
	}
	if len(moves) == 9 {
		return "Draw"
	}
	return "Pending"
}
