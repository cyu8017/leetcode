// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

func countPyramids(grid [][]int) int {
	count := func(g [][]int) int {
		m, n := len(g), len(g[0])
		dp := make([][]int, m)
		for i := range dp {
			dp[i] = make([]int, n)
			copy(dp[i], g[i])
		}
		ans := 0
		for i := m - 2; i >= 0; i-- {
			for j := 1; j < n-1; j++ {
				if g[i][j] == 1 {
					dp[i][j] = 1 + min(dp[i+1][j-1], min(dp[i+1][j], dp[i+1][j+1]))
					ans += dp[i][j] - 1
				}
			}
		}
		return ans
	}
	ans := count(grid)
	// reverse vertically for inverse pyramids
	m := len(grid)
	rev := make([][]int, m)
	for i := 0; i < m; i++ {
		rev[i] = grid[m-1-i]
	}
	return ans + count(rev)
}
