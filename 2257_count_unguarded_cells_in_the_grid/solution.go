// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
	grid := make([][]int, m)
	for i := range grid {
		grid[i] = make([]int, n)
	}
	for _, w := range walls {
		grid[w[0]][w[1]] = 2
	}
	for _, g := range guards {
		grid[g[0]][g[1]] = 2
	}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for _, g := range guards {
		for _, d := range dirs {
			r, c := g[0]+d[0], g[1]+d[1]
			for r >= 0 && r < m && c >= 0 && c < n && grid[r][c] != 2 {
				grid[r][c] = 1
				r += d[0]
				c += d[1]
			}
		}
	}
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 0 {
				ans++
			}
		}
	}
	return ans
}
