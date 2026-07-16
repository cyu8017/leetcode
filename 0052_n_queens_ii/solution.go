// LeetCode 0052 - N-Queens II
// https://leetcode.com/problems/n-queens-ii/

func totalNQueens(n int) int {
	count := 0
	cols := make(map[int]bool)
	diag1 := make(map[int]bool)
	diag2 := make(map[int]bool)

	var backtrack func(row int)
	backtrack = func(row int) {
		if row == n {
			count++
			return
		}

		for col := 0; col < n; col++ {
			if cols[col] || diag1[row+col] || diag2[row-col] {
				continue
			}

			cols[col] = true
			diag1[row+col] = true
			diag2[row-col] = true
			backtrack(row + 1)
			delete(cols, col)
			delete(diag1, row+col)
			delete(diag2, row-col)
		}
	}

	backtrack(0)
	return count
}
