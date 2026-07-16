// LeetCode 0348 - Design Tic-Tac-Toe
// https://leetcode.com/problems/design-tic-tac-toe/

type TicTacToe struct {
	n         int
	rows      []int
	cols      []int
	diag      int
	antiDiag  int
}

func Constructor(n int) TicTacToe {
	return TicTacToe{
		n:    n,
		rows: make([]int, n),
		cols: make([]int, n),
	}
}

func (this *TicTacToe) Move(row int, col int, player int) int {
	add := 1
	if player != 1 {
		add = -1
	}

	this.rows[row] += add
	this.cols[col] += add
	if row == col {
		this.diag += add
	}
	if row+col == this.n-1 {
		this.antiDiag += add
	}

	if abs(this.rows[row]) == this.n ||
		abs(this.cols[col]) == this.n ||
		abs(this.diag) == this.n ||
		abs(this.antiDiag) == this.n {
		return player
	}

	return 0
}

func abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}
