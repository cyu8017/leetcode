// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

func uniquePathsIII(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	empty, sr, sc := 0, 0, 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] != -1 {
				empty++
			}
			if grid[i][j] == 1 {
				sr, sc = i, j
			}
		}
	}
	ans := 0
	var dfs func(r, c, remain int)
	dfs = func(r, c, remain int) {
		if grid[r][c] == 2 {
			if remain == 1 {
				ans++
			}
			return
		}
		temp := grid[r][c]
		grid[r][c] = -1
		for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != -1 {
				dfs(nr, nc, remain-1)
			}
		}
		grid[r][c] = temp
	}
	dfs(sr, sc, empty)
	return ans
}
