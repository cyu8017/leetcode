// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

func hitBricks(grid [][]int, hits [][]int) []int {
	m, n := len(grid), len(grid[0])
	roof := m * n
	parent := make([]int, roof+1)
	size := make([]int, roof+1)
	for i := range parent {
		parent[i] = i
		size[i] = 1
	}
	find := func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	union := func(a, b int) {
		ra, rb := find(a), find(b)
		if ra == rb {
			return
		}
		parent[ra] = rb
		size[rb] += size[ra]
	}
	idx := func(r, c int) int { return r*n + c }
	status := make([][]int, m)
	for i := range grid {
		status[i] = append([]int{}, grid[i]...)
	}
	for _, h := range hits {
		status[h[0]][h[1]] = 0
	}
	dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if status[r][c] == 0 {
				continue
			}
			if r == 0 {
				union(idx(r, c), roof)
			}
			for _, d := range dirs {
				nr, nc := r+d[0], c+d[1]
				if nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1 {
					union(idx(r, c), idx(nr, nc))
				}
			}
		}
	}
	answer := make([]int, len(hits))
	for i := len(hits) - 1; i >= 0; i-- {
		r, c := hits[i][0], hits[i][1]
		if grid[r][c] == 0 {
			continue
		}
		prev := size[find(roof)]
		status[r][c] = 1
		if r == 0 {
			union(idx(r, c), roof)
		}
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1 {
				union(idx(r, c), idx(nr, nc))
			}
		}
		curr := size[find(roof)]
		diff := curr - prev - 1
		if diff > 0 {
			answer[i] = diff
		}
	}
	return answer
}
