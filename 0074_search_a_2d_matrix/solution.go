// LeetCode 0074 - Search a 2D Matrix
// https://leetcode.com/problems/search-a-2d-matrix/

func searchMatrix(matrix [][]int, target int) bool {
	row := 0
	col := len(matrix[0]) - 1

	for row < len(matrix) && col >= 0 {
		if matrix[row][col] == target {
			return true
		}
		if matrix[row][col] > target {
			col--
		} else {
			row++
		}
	}

	return false
}
