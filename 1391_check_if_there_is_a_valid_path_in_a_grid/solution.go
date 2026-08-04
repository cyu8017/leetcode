// LeetCode 1391 - Check if There is a Valid Path in a Grid
// https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

func hasValidPath(grid [][]int) bool {
	dirs := map[int][][2]int{
		1: {{0, -1}, {0, 1}},
		2: {{-1, 0}, {1, 0}},
		3: {{0, -1}, {1, 0}},
		4: {{0, 1}, {1, 0}},
		5: {{0, -1}, {-1, 0}},
		6: {{0, 1}, {-1, 0}},
	}
	m, n := len(grid), len(grid[0])
	seen := map[[2]int]bool{{0, 0}: true}
	st := [][2]int{{0, 0}}
	for len(st) > 0 {
		cur := st[len(st)-1]
		st = st[:len(st)-1]
		r, c := cur[0], cur[1]
		if r == m-1 && c == n-1 {
			return true
		}
		for _, d := range dirs[grid[r][c]] {
			x, y := r+d[0], c+d[1]
			if x >= 0 && x < m && y >= 0 && y < n && !seen[[2]int{x, y}] {
				ok := false
				for _, back := range dirs[grid[x][y]] {
					if back[0] == -d[0] && back[1] == -d[1] {
						ok = true
						break
					}
				}
				if ok {
					seen[[2]int{x, y}] = true
					st = append(st, [2]int{x, y})
				}
			}
		}
	}
	return false
}
