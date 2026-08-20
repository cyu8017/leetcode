// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/


func findMaxFish(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	var dfs func(r, c int) int
	dfs = func(r, c int) int {
		if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 {
			return 0
		}
		fish := grid[r][c]
		grid[r][c] = 0
		return fish + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
	}
	best := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] > 0 {
				if v := dfs(i, j); v > best {
					best = v
				}
			}
		}
	}
	return best
}
