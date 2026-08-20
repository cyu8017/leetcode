// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/


func tourOfKnight(m int, n int, r int, c int) [][]int {
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
		for j := range ans[i] {
			ans[i][j] = -1
		}
	}
	dirs := [][2]int{{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}}
	var dfs func(x, y, step int) bool
	dfs = func(x, y, step int) bool {
		ans[x][y] = step
		if step == m*n-1 {
			return true
		}
		for _, d := range dirs {
			nx, ny := x+d[0], y+d[1]
			if nx >= 0 && nx < m && ny >= 0 && ny < n && ans[nx][ny] == -1 {
				if dfs(nx, ny, step+1) {
					return true
				}
			}
		}
		ans[x][y] = -1
		return false
	}
	dfs(r, c, 0)
	return ans
}
