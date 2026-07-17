// LeetCode 1730 - Shortest Path to Get Food
// https://leetcode.com/problems/shortest-path-to-get-food/

func getFood(grid [][]byte) int {
	rows, cols := len(grid), len(grid[0])
	type entry struct{ r, c, d int }
	queue := make([]entry, 0, rows*cols)
	seen := make([][]bool, rows)
	for r := range seen {
		seen[r] = make([]bool, cols)
	}
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] == '*' {
				queue = append(queue, entry{r, c, 0})
				seen[r][c] = true
			}
		}
	}
	dirs := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for head := 0; head < len(queue); head++ {
		cur := queue[head]
		if grid[cur.r][cur.c] == '#' {
			return cur.d
		}
		for _, dir := range dirs {
			nr, nc := cur.r+dir[0], cur.c+dir[1]
			if nr >= 0 && nr < rows && nc >= 0 && nc < cols && !seen[nr][nc] && grid[nr][nc] != 'X' {
				seen[nr][nc] = true
				queue = append(queue, entry{nr, nc, cur.d + 1})
			}
		}
	}
	return -1
}
