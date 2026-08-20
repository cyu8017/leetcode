// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/


func checkValidGrid(grid [][]int) bool {
	n := len(grid)
	if grid[0][0] != 0 {
		return false
	}
	pos := make([][2]int, n*n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			pos[grid[i][j]] = [2]int{i, j}
		}
	}
	dirs := [][2]int{{1, 2}, {1, -2}, {-1, 2}, {-1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}}
	for v := 0; v+1 < n*n; v++ {
		r, c := pos[v][0], pos[v][1]
		ok := false
		for _, d := range dirs {
			if r+d[0] == pos[v+1][0] && c+d[1] == pos[v+1][1] {
				ok = true
				break
			}
		}
		if !ok {
			return false
		}
	}
	return true
}
