// LeetCode 0766 - Toeplitz Matrix
// https://leetcode.com/problems/toeplitz-matrix/

func isToeplitzMatrix(matrix [][]int) bool {
	for r := 1; r < len(matrix); r++ {
		for c := 1; c < len(matrix[0]); c++ {
			if matrix[r][c] != matrix[r-1][c-1] {
				return false
			}
		}
	}
	return true
}
