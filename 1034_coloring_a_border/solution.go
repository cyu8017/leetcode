// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

func colorBorder(grid [][]int, row, col, color int) [][]int {
	m, n := len(grid), len(grid[0])
	original := grid[row][col]
	component := map[[2]int]bool{[2]int{row, col}: true}
	stack := [][2]int{{row, col}}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		r, c := cur[0], cur[1]
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			key := [2]int{nr, nc}
			if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == original && !component[key] {
				component[key] = true
				stack = append(stack, key)
			}
		}
	}
	border := [][2]int{}
	for key := range component {
		r, c := key[0], key[1]
		isBorder := false
		for _, d := range dirs {
			nr, nc := r+d[0], c+d[1]
			if !(nr >= 0 && nr < m && nc >= 0 && nc < n) || !component[[2]int{nr, nc}] {
				isBorder = true
				break
			}
		}
		if isBorder {
			border = append(border, key)
		}
	}
	for _, key := range border {
		grid[key[0]][key[1]] = color
	}
	return grid
}
