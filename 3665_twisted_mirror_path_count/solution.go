// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

func uniquePaths(grid [][]int) int {
	const MOD = 1_000_000_007
	m := len(grid)
	n := len(grid[0])
	// dp[i][j] = ways to reach empty cell (i,j)
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	if grid[0][0] == 1 {
		return 0
	}
	dp[0][0] = 1
	// For each empty cell, propagate to next empty cells via moves/reflections
	type pair struct{ i, j int }
	nextCell := func(i, j, di, dj int) (int, int, bool) {
		ni, nj := i+di, j+dj
		for ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1 {
			// reflect: right->down, down->right
			if dj == 1 {
				di, dj = 1, 0
			} else {
				di, dj = 0, 1
			}
			ni, nj = ni+di, nj+dj
		}
		if ni < 0 || nj < 0 || ni >= m || nj >= n {
			return 0, 0, false
		}
		return ni, nj, true
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 || dp[i][j] == 0 {
				continue
			}
			if ni, nj, ok := nextCell(i, j, 0, 1); ok {
				dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD
			}
			if ni, nj, ok := nextCell(i, j, 1, 0); ok {
				dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD
			}
		}
	}
	return dp[m-1][n-1]
}
