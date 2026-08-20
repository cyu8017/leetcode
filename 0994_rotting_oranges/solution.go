// LeetCode 0994 - Rotting Oranges
// https://leetcode.com/problems/rotting-oranges/

func orangesRotting(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	type cell struct{ r, c int }
	queue := []cell{}
	fresh := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 2 {
				queue = append(queue, cell{i, j})
			} else if grid[i][j] == 1 {
				fresh++
			}
		}
	}
	minutes := 0
	for len(queue) > 0 && fresh > 0 {
		sz := len(queue)
		for k := 0; k < sz; k++ {
			cur := queue[0]
			queue = queue[1:]
			for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
				nr, nc := cur.r+d[0], cur.c+d[1]
				if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1 {
					grid[nr][nc] = 2
					fresh--
					queue = append(queue, cell{nr, nc})
				}
			}
		}
		minutes++
	}
	if fresh == 0 {
		return minutes
	}
	return -1
}
