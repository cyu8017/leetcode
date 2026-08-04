// LeetCode 1559 - Detect Cycles in 2D Grid
// https://leetcode.com/problems/detect-cycles-in-2d-grid/

func containsCycle(grid [][]byte) bool {
	m, n := len(grid), len(grid[0])
	seen := make([][]bool, m)
	for i := range seen {
		seen[i] = make([]bool, n)
	}
	var dfs func(r, c, pr, pc int) bool
	dfs = func(r, c, pr, pc int) bool {
		seen[r][c] = true
		dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] != grid[r][c] || (nr == pr && nc == pc) {
				continue
			}
			if seen[nr][nc] || dfs(nr, nc, r, c) {
				return true
			}
		}
		return false
	}
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if !seen[r][c] && dfs(r, c, -1, -1) {
				return true
			}
		}
	}
	return false
}
