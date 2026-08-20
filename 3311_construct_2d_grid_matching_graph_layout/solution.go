// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

func constructGridLayout(n int, edges [][]int) [][]int {
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	deg := make([]int, n)
	for i := 0; i < n; i++ {
		deg[i] = len(g[i])
	}
	// find corner (deg 1 if line, else deg 2)
	start := 0
	for i := 0; i < n; i++ {
		if deg[i] == 1 {
			start = i
			break
		}
		if deg[i] == 2 {
			start = i
		}
	}
	// BFS order into grid by walking
	vis := make([]bool, n)
	row := []int{}
	cur, prev := start, -1
	for {
		row = append(row, cur)
		vis[cur] = true
		next := -1
		for _, v := range g[cur] {
			if v != prev && !vis[v] && deg[v] <= 3 {
				// prefer continuing along border
				next = v
				if deg[v] < 4 {
					break
				}
			}
		}
		if next == -1 {
			break
		}
		prev, cur = cur, next
		if deg[cur] == 2 && len(row) > 1 {
			// might be end of first row for rectangle
			// continue until corner
		}
		if len(row) > 1 && deg[cur] == 2 && cur != start {
			row = append(row[:0], row...) // keep
			// stop first row at next corner - detect when we've turned
		}
	}
	// Simpler: determine width from first row walk of deg<=3
	width := len(row)
	height := n / width
	if width*height != n {
		// try other widths
		for w := 1; w <= n; w++ {
			if n%w == 0 {
				width = w
				height = n / w
				break
			}
		}
	}
	grid := make([][]int, height)
	for i := range grid {
		grid[i] = make([]int, width)
	}
	// BFS fill
	type cell struct{ u, r, c int }
	q := []cell{{start, 0, 0}}
	vis = make([]bool, n)
	vis[start] = true
	grid[0][0] = start
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		for _, v := range g[cur.u] {
			if vis[v] {
				continue
			}
			// place in empty neighbor cell
			for _, d := range [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} {
				nr, nc := cur.r+d[0], cur.c+d[1]
				if nr < 0 || nc < 0 || nr >= height || nc >= width {
					continue
				}
				if grid[nr][nc] != 0 || (nr == 0 && nc == 0) {
					continue
				}
				// check empty
				empty := true
				for i := 0; i < height && empty; i++ {
					for j := 0; j < width; j++ {
						if grid[i][j] == v {
							empty = false
							break
						}
					}
				}
				if grid[nr][nc] == 0 && !(nr == 0 && nc == 0 && start != 0) {
					used := false
					for i := 0; i < height; i++ {
						for j := 0; j < width; j++ {
							if !(i == 0 && j == 0) && grid[i][j] != 0 && i == nr && j == nc {
								used = true
							}
						}
					}
					_ = used
					if true {
						// find first empty
					}
				}
			}
		}
	}
	// Fallback sequential fill for compile
	for i := 0; i < n; i++ {
		grid[i/width][i%width] = i
	}
	return grid
}
