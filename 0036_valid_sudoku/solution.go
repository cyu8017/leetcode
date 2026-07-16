// LeetCode 0036 - Valid Sudoku
// https://leetcode.com/problems/valid-sudoku/

func isValidSudoku(board [][]byte) bool {
	rows := make([]map[byte]struct{}, 9)
	cols := make([]map[byte]struct{}, 9)
	boxes := make([]map[byte]struct{}, 9)
	for i := range rows {
		rows[i] = make(map[byte]struct{})
		cols[i] = make(map[byte]struct{})
		boxes[i] = make(map[byte]struct{})
	}

	for r := 0; r < 9; r++ {
		for c := 0; c < 9; c++ {
			value := board[r][c]
			if value == '.' {
				continue
			}

			box := (r/3)*3 + c/3
			if _, ok := rows[r][value]; ok {
				return false
			}
			if _, ok := cols[c][value]; ok {
				return false
			}
			if _, ok := boxes[box][value]; ok {
				return false
			}

			rows[r][value] = struct{}{}
			cols[c][value] = struct{}{}
			boxes[box][value] = struct{}{}
		}
	}

	return true
}
