// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

func countPaths(grid [][]int) int {
	const mod = 1000000007
	m, n := len(grid), len(grid[0])
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	var dfs func(int, int) int
	dfs = func(r, c int) int {
		if dp[r][c] != 0 {
			return dp[r][c]
		}
		res := 1
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > grid[r][c] {
				res = (res + dfs(nr, nc)) % mod
			}
		}
		dp[r][c] = res
		return res
	}
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			ans = (ans + dfs(i, j)) % mod
		}
	}
	return ans
}
