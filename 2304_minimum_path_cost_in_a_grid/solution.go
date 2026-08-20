// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

func minPathCost(grid [][]int, moveCost [][]int) int {
	m, n := len(grid), len(grid[0])
	dp := make([]int, n)
	copy(dp, grid[0])
	for r := 0; r < m-1; r++ {
		next := make([]int, n)
		for j := range next {
			next[j] = 1 << 30
		}
		for c := 0; c < n; c++ {
			from := grid[r][c]
			for nc := 0; nc < n; nc++ {
				cost := dp[c] + moveCost[from][nc] + grid[r+1][nc]
				if cost < next[nc] {
					next[nc] = cost
				}
			}
		}
		dp = next
	}
	ans := dp[0]
	for i := 1; i < n; i++ {
		if dp[i] < ans {
			ans = dp[i]
		}
	}
	return ans
}
