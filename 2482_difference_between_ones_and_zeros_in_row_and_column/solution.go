// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

func onesMinusZeros(grid [][]int) [][]int {
	m, n := len(grid), len(grid[0])
	row := make([]int, m)
	col := make([]int, n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			row[i] += grid[i][j]
			col[j] += grid[i][j]
		}
	}
	ans := make([][]int, m)
	for i := 0; i < m; i++ {
		ans[i] = make([]int, n)
		for j := 0; j < n; j++ {
			ans[i][j] = row[i] + col[j] - (m - row[i]) - (n - col[j])
		}
	}
	return ans
}
