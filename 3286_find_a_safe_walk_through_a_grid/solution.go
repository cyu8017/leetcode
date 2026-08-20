// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

func findSafeWalk(grid [][]int, health int) bool {
	m, n := len(grid), len(grid[0])
	type st struct{ r, c, h int }
	vis := make([][]int, m)
	for i := range vis {
		vis[i] = make([]int, n)
		for j := range vis[i] {
			vis[i][j] = -1
		}
	}
	qh := health - grid[0][0]
	if qh <= 0 {
		return false
	}
	q := []st{{0, 0, qh}}
	vis[0][0] = qh
	dirs := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.r == m-1 && cur.c == n-1 {
			return true
		}
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr < 0 || nc < 0 || nr >= m || nc >= n {
				continue
			}
			nh := cur.h - grid[nr][nc]
			if nh <= 0 {
				continue
			}
			if nh > vis[nr][nc] {
				vis[nr][nc] = nh
				q = append(q, st{nr, nc, nh})
			}
		}
	}
	return false
}
