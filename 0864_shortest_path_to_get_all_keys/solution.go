// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

func shortestPathAllKeys(grid []string) int {
	m, n := len(grid), len(grid[0])
	allKeys := 0
	sr, sc := 0, 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			ch := grid[i][j]
			if ch == '@' {
				sr, sc = i, j
			} else if ch >= 'a' && ch <= 'f' {
				allKeys |= 1 << (ch - 'a')
			}
		}
	}
	type state struct{ r, c, mask, dist int }
	queue := []state{{sr, sc, 0, 0}}
	seen := map[[3]int]bool{{sr, sc, 0}: true}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.mask == allKeys {
			return cur.dist
		}
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == '#' {
				continue
			}
			cell := grid[nr][nc]
			nmask := cur.mask
			if cell >= 'a' && cell <= 'f' {
				nmask |= 1 << (cell - 'a')
			}
			if cell >= 'A' && cell <= 'F' && cur.mask&(1<<(cell-'A')) == 0 {
				continue
			}
			key := [3]int{nr, nc, nmask}
			if !seen[key] {
				seen[key] = true
				queue = append(queue, state{nr, nc, nmask, cur.dist + 1})
			}
		}
	}
	return -1
}
