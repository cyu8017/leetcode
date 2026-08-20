// LeetCode 2133 - Check if Every Row and Column Contains All Numbers
// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

func checkValid(matrix [][]int) bool {
	n := len(matrix)
	for i := 0; i < n; i++ {
		row, col := make([]bool, n+1), make([]bool, n+1)
		for j := 0; j < n; j++ {
			if row[matrix[i][j]] || col[matrix[j][i]] {
				return false
			}
			row[matrix[i][j]] = true
			col[matrix[j][i]] = true
		}
	}
	return true
}
