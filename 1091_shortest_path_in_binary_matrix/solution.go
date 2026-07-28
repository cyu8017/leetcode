// LeetCode 1091 - Shortest Path in Binary Matrix
// https://leetcode.com/problems/shortest-path-in-binary-matrix/

func shortestPathBinaryMatrix(grid [][]int) int {
	n := len(grid)
	if grid[0][0] != 0 || grid[n-1][n-1] != 0 {
		return -1
	}
	type cell struct{ r, c, dist int }
	queue := []cell{{0, 0, 1}}
	grid[0][0] = 1
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.r == n-1 && cur.c == n-1 {
			return cur.dist
		}
		for dr := -1; dr <= 1; dr++ {
			for dc := -1; dc <= 1; dc++ {
				if dr == 0 && dc == 0 {
					continue
				}
				nr, nc := cur.r+dr, cur.c+dc
				if nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0 {
					grid[nr][nc] = 1
					queue = append(queue, cell{nr, nc, cur.dist + 1})
				}
			}
		}
	}
	return -1
}
