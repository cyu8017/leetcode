// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

func shortestPath(grid [][]int, k int) int {
	m, n := len(grid), len(grid[0])
	if k >= m+n-2 {
		return m + n - 2
	}
	type item struct{ r, c, rem, dist int }
	q := []item{{0, 0, k, 0}}
	best := map[[2]int]int{{0, 0}: k}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.r == m-1 && cur.c == n-1 {
			return cur.dist
		}
		for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n {
				nxt := cur.rem - grid[nr][nc]
				key := [2]int{nr, nc}
				if nxt >= 0 && nxt > best[key] {
					best[key] = nxt
					q = append(q, item{nr, nc, nxt, cur.dist + 1})
				}
			}
		}
	}
	return -1
}
