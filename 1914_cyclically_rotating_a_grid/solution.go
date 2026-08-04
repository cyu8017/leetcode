// LeetCode 1914 - Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

func rotateGrid(grid [][]int, k int) [][]int {
	m, n := len(grid), len(grid[0])
	layers := m
	if n < layers {
		layers = n
	}
	layers /= 2
	for layer := 0; layer < layers; layer++ {
		vals := []int{}
		for c := layer; c < n-layer; c++ {
			vals = append(vals, grid[layer][c])
		}
		for r := layer + 1; r < m-layer; r++ {
			vals = append(vals, grid[r][n-layer-1])
		}
		if m-2*layer > 1 {
			for c := n - layer - 2; c >= layer; c-- {
				vals = append(vals, grid[m-layer-1][c])
			}
		}
		if n-2*layer > 1 {
			for r := m - layer - 2; r > layer; r-- {
				vals = append(vals, grid[r][layer])
			}
		}
		shift := k % len(vals)
		vals = append(vals[shift:], vals[:shift]...)
		idx := 0
		for c := layer; c < n-layer; c++ {
			grid[layer][c] = vals[idx]
			idx++
		}
		for r := layer + 1; r < m-layer; r++ {
			grid[r][n-layer-1] = vals[idx]
			idx++
		}
		if m-2*layer > 1 {
			for c := n - layer - 2; c >= layer; c-- {
				grid[m-layer-1][c] = vals[idx]
				idx++
			}
		}
		if n-2*layer > 1 {
			for r := m - layer - 2; r > layer; r-- {
				grid[r][layer] = vals[idx]
				idx++
			}
		}
	}
	return grid
}
