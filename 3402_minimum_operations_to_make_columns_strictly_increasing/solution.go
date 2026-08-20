// LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
// https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

func minimumOperations(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	ans := 0
	for j := 0; j < n; j++ {
		for i := 1; i < m; i++ {
			if grid[i][j] <= grid[i-1][j] {
				need := grid[i-1][j] + 1
				ans += need - grid[i][j]
				grid[i][j] = need
			}
		}
	}
	return ans
}
