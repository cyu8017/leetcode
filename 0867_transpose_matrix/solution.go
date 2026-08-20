// LeetCode 0867 - Transpose Matrix
// https://leetcode.com/problems/transpose-matrix/

func transpose(matrix [][]int) [][]int {
	m, n := len(matrix), len(matrix[0])
	ans := make([][]int, n)
	for j := 0; j < n; j++ {
		ans[j] = make([]int, m)
		for i := 0; i < m; i++ {
			ans[j][i] = matrix[i][j]
		}
	}
	return ans
}
