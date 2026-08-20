// LeetCode 2428 - Maximum Sum of an Hourglass
// https://leetcode.com/problems/maximum-sum-of-an-hourglass/

func maxSum(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	ans := 0
	for i := 0; i+2 < m; i++ {
		for j := 0; j+2 < n; j++ {
			s := grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
			if s > ans {
				ans = s
			}
		}
	}
	return ans
}
