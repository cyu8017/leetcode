// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

func placeWordInCrossword(board [][]byte, word string) bool {
	m, n := len(board), len(board[0])
	L := len(word)
	match := func(cells []byte) bool {
		if len(cells) != L {
			return false
		}
		ok1, ok2 := true, true
		for i := 0; i < L; i++ {
			if cells[i] != ' ' && cells[i] != word[i] {
				ok1 = false
			}
			if cells[i] != ' ' && cells[i] != word[L-1-i] {
				ok2 = false
			}
		}
		return ok1 || ok2
	}
	for r := 0; r < m; r++ {
		c := 0
		for c < n {
			for c < n && board[r][c] == '#' {
				c++
			}
			start := c
			for c < n && board[r][c] != '#' {
				c++
			}
			if c-start == L {
				cells := make([]byte, L)
				copy(cells, board[r][start:c])
				if match(cells) {
					return true
				}
			}
		}
	}
	for c := 0; c < n; c++ {
		r := 0
		for r < m {
			for r < m && board[r][c] == '#' {
				r++
			}
			start := r
			for r < m && board[r][c] != '#' {
				r++
			}
			if r-start == L {
				cells := make([]byte, L)
				for i := 0; i < L; i++ {
					cells[i] = board[start+i][c]
				}
				if match(cells) {
					return true
				}
			}
		}
	}
	return false
}
