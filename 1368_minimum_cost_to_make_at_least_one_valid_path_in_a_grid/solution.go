// LeetCode 1368 - Minimum Cost to Make at Least One Valid Path in a Grid
// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

func minCost(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	const inf = int(1e9)
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = inf
		}
	}
	dist[0][0] = 0
	type pair struct{ r, c int }
	dq := []pair{{0, 0}}
	dirs := [][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	for len(dq) > 0 {
		cur := dq[0]
		dq = dq[1:]
		r, c := cur.r, cur.c
		for k, d := range dirs {
			x, y := r+d[0], c+d[1]
			if x >= 0 && x < m && y >= 0 && y < n {
				w := 0
				if k+1 != grid[r][c] {
					w = 1
				}
				nd := dist[r][c] + w
				if nd < dist[x][y] {
					dist[x][y] = nd
					if w == 0 {
						dq = append([]pair{{x, y}}, dq...)
					} else {
						dq = append(dq, pair{x, y})
					}
				}
			}
		}
	}
	return dist[m-1][n-1]
}
