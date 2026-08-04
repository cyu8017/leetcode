// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

func getMaximumGold(grid [][]int) int {
	rows, cols := len(grid), len(grid[0])
	var dfs func(int, int) int
	dfs = func(r, c int) int {
		gold := grid[r][c]
		grid[r][c] = 0
		best := 0
		for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] > 0 {
				v := dfs(nr, nc)
				if v > best {
					best = v
				}
			}
		}
		grid[r][c] = gold
		return gold + best
	}
	ans := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] > 0 {
				v := dfs(r, c)
				if v > ans {
					ans = v
				}
			}
		}
	}
	return ans
}
