// LeetCode 0498 - Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse/

func findDiagonalOrder(mat [][]int) []int {
	if len(mat) == 0 || len(mat[0]) == 0 {
		return nil
	}
	rows := len(mat)
	cols := len(mat[0])
	result := make([]int, 0, rows*cols)
	row, col := 0, 0
	upward := true
	for count := 0; count < rows*cols; count++ {
		result = append(result, mat[row][col])
		if upward {
			if col == cols-1 {
				row++
				upward = false
			} else if row == 0 {
				col++
				upward = false
			} else {
				row--
				col++
			}
		} else {
			if row == rows-1 {
				col++
				upward = true
			} else if col == 0 {
				row++
				upward = true
			} else {
				row++
				col--
			}
		}
	}
	return result
}
