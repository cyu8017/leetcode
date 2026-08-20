// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

func validTicTacToe(board []string) bool {
	flat := board[0] + board[1] + board[2]
	xCount, oCount := 0, 0
	for i := 0; i < len(flat); i++ {
		if flat[i] == 'X' {
			xCount++
		} else if flat[i] == 'O' {
			oCount++
		}
	}
	if oCount != xCount && oCount != xCount-1 {
		return false
	}
	win := func(player byte) bool {
		p := string([]byte{player, player, player})
		lines := []string{board[0], board[1], board[2]}
		for c := 0; c < 3; c++ {
			lines = append(lines, string([]byte{board[0][c], board[1][c], board[2][c]}))
		}
		lines = append(lines, string([]byte{board[0][0], board[1][1], board[2][2]}))
		lines = append(lines, string([]byte{board[0][2], board[1][1], board[2][0]}))
		for _, line := range lines {
			if line == p {
				return true
			}
		}
		return false
	}
	xWin, oWin := win('X'), win('O')
	if xWin && oWin {
		return false
	}
	if xWin && xCount != oCount+1 {
		return false
	}
	if oWin && xCount != oCount {
		return false
	}
	return true
}
