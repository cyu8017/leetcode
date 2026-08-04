// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

func maxDistance(grid [][]int) int {
	n := len(grid)
	type cell struct{ r, c int }
	queue := []cell{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				queue = append(queue, cell{i, j})
			}
		}
	}
	if len(queue) == 0 || len(queue) == n*n {
		return -1
	}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	dist := -1
	for len(queue) > 0 {
		size := len(queue)
		dist++
		for i := 0; i < size; i++ {
			cur := queue[0]
			queue = queue[1:]
			for _, d := range dirs {
				nr, nc := cur.r+d[0], cur.c+d[1]
				if nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0 {
					grid[nr][nc] = 1
					queue = append(queue, cell{nr, nc})
				}
			}
		}
	}
	return dist
}
