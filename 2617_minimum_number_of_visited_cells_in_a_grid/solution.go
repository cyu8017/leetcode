// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/


func minimumVisitedCells(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = -1
		}
	}
	type cell struct{ r, c int }
	q := []cell{{0, 0}}
	dist[0][0] = 1
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		r, c := cur.r, cur.c
		if r == m-1 && c == n-1 {
			return dist[r][c]
		}
		for nc := c + 1; nc <= c+grid[r][c] && nc < n; nc++ {
			if dist[r][nc] == -1 {
				dist[r][nc] = dist[r][c] + 1
				q = append(q, cell{r, nc})
			}
		}
		for nr := r + 1; nr <= r+grid[r][c] && nr < m; nr++ {
			if dist[nr][c] == -1 {
				dist[nr][c] = dist[r][c] + 1
				q = append(q, cell{nr, c})
			}
		}
	}
	return -1
}
