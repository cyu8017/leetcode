// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

func minimumObstacles(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = 1 << 30
		}
	}
	dist[0][0] = 0
	type node struct{ r, c int }
	dq := []node{{0, 0}}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(dq) > 0 {
		cur := dq[0]
		dq = dq[1:]
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr < 0 || nr >= m || nc < 0 || nc >= n {
				continue
			}
			nd := dist[cur.r][cur.c] + grid[nr][nc]
			if nd < dist[nr][nc] {
				dist[nr][nc] = nd
				if grid[nr][nc] == 0 {
					dq = append([]node{{nr, nc}}, dq...)
				} else {
					dq = append(dq, node{nr, nc})
				}
			}
		}
	}
	return dist[m-1][n-1]
}
