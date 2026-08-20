// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

func maxAreaOfIsland(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	var dfs func(r, c int) int
	dfs = func(r, c int) int {
		if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 {
			return 0
		}
		grid[r][c] = 0
		return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
	}
	best := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			area := dfs(i, j)
			if area > best {
				best = area
			}
		}
	}
	return best
}
