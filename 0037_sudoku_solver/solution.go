// LeetCode 0037 - Sudoku Solver
// https://leetcode.com/problems/sudoku-solver/

func solveSudoku(board [][]byte) {
	rows := make([]map[byte]struct{}, 9)
	cols := make([]map[byte]struct{}, 9)
	boxes := make([]map[byte]struct{}, 9)
	for i := range rows {
		rows[i] = make(map[byte]struct{})
		cols[i] = make(map[byte]struct{})
		boxes[i] = make(map[byte]struct{})
	}

	empty := make([][2]int, 0)
	for r := 0; r < 9; r++ {
		for c := 0; c < 9; c++ {
			value := board[r][c]
			if value == '.' {
				empty = append(empty, [2]int{r, c})
				continue
			}
			box := (r/3)*3 + c/3
			rows[r][value] = struct{}{}
			cols[c][value] = struct{}{}
			boxes[box][value] = struct{}{}
		}
	}

	var backtrack func(index int) bool
	backtrack = func(index int) bool {
		if index == len(empty) {
			return true
		}

		r, c := empty[index][0], empty[index][1]
		box := (r/3)*3 + c/3
		for digit := byte('1'); digit <= '9'; digit++ {
			if _, ok := rows[r][digit]; ok {
				continue
			}
			if _, ok := cols[c][digit]; ok {
				continue
			}
			if _, ok := boxes[box][digit]; ok {
				continue
			}

			board[r][c] = digit
			rows[r][digit] = struct{}{}
			cols[c][digit] = struct{}{}
			boxes[box][digit] = struct{}{}

			if backtrack(index + 1) {
				return true
			}

			board[r][c] = '.'
			delete(rows[r], digit)
			delete(cols[c], digit)
			delete(boxes[box], digit)
		}

		return false
	}

	backtrack(0)
}
