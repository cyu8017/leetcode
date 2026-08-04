// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

func countSubIslands(grid1 [][]int, grid2 [][]int) int {
	rows, cols := len(grid2), len(grid2[0])
	var dfs func(r, c int) bool
	dfs = func(r, c int) bool {
		if r < 0 || c < 0 || r >= rows || c >= cols || grid2[r][c] == 0 {
			return true
		}
		grid2[r][c] = 0
		ok := grid1[r][c] == 1
		for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
			if !dfs(r+d[0], c+d[1]) {
				ok = false
			}
		}
		return ok
	}
	ans := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid2[r][c] == 1 && dfs(r, c) {
				ans++
			}
		}
	}
	return ans
}
