// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

func countSquares(matrix [][]int) int {
	answer := 0
	for r := 0; r < len(matrix); r++ {
		for c := 0; c < len(matrix[0]); c++ {
			if matrix[r][c] > 0 && r > 0 && c > 0 {
				m := matrix[r-1][c]
				if matrix[r][c-1] < m {
					m = matrix[r][c-1]
				}
				if matrix[r-1][c-1] < m {
					m = matrix[r-1][c-1]
				}
				matrix[r][c] += m
			}
			answer += matrix[r][c]
		}
	}
	return answer
}
