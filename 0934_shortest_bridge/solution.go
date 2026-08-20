// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

func shortestBridge(grid [][]int) int {
	n := len(grid)
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	var dfs func(int, int)
	dfs = func(r, c int) {
		if r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1 {
			return
		}
		grid[r][c] = 2
		for _, d := range dirs {
			dfs(r+d[0], c+d[1])
		}
	}
	found := false
	for i := 0; i < n && !found; i++ {
		for j := 0; j < n && !found; j++ {
			if grid[i][j] == 1 {
				dfs(i, j)
				found = true
			}
		}
	}
	type cell struct{ r, c, dist int }
	queue := []cell{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 2 {
				queue = append(queue, cell{i, j, 0})
			}
		}
	}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < n && nc >= 0 && nc < n {
				if grid[nr][nc] == 1 {
					return cur.dist
				}
				if grid[nr][nc] == 0 {
					grid[nr][nc] = 2
					queue = append(queue, cell{nr, nc, cur.dist + 1})
				}
			}
		}
	}
	return -1
}
