// LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
// https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

func minimumOperations(grid [][]int) int {
	// bipartite matching on 1-cells (checkerboard)
	m, n := len(grid), len(grid[0])
	id := make([][]int, m)
	cnt := 0
	for i := 0; i < m; i++ {
		id[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				id[i][j] = cnt
				cnt++
			} else {
				id[i][j] = -1
			}
		}
	}
	g := make([][]int, cnt)
	dirs := [][2]int{{0, 1}, {1, 0}}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] != 1 || (i+j)%2 != 0 {
				continue
			}
			u := id[i][j]
			for _, d := range dirs {
				ni, nj := i+d[0], j+d[1]
				if ni < m && nj < n && grid[ni][nj] == 1 {
					g[u] = append(g[u], id[ni][nj])
				}
			}
			// also left/up already covered by others; add all 4 for safety from black
			for _, d := range [][2]int{{0, -1}, {-1, 0}} {
				ni, nj := i+d[0], j+d[1]
				if ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1 {
					g[u] = append(g[u], id[ni][nj])
				}
			}
		}
	}
	match := make([]int, cnt)
	for i := range match {
		match[i] = -1
	}
	var dfs func(u int, seen []bool) bool
	dfs = func(u int, seen []bool) bool {
		for _, v := range g[u] {
			if seen[v] {
				continue
			}
			seen[v] = true
			if match[v] == -1 || dfs(match[v], seen) {
				match[v] = u
				return true
			}
		}
		return false
	}
	ans := 0
	for u := 0; u < cnt; u++ {
		// only left side
		ok := false
		for i := 0; i < m && !ok; i++ {
			for j := 0; j < n; j++ {
				if id[i][j] == u && (i+j)%2 == 0 {
					ok = true
					break
				}
			}
		}
		if !ok {
			continue
		}
		seen := make([]bool, cnt)
		if dfs(u, seen) {
			ans++
		}
	}
	return ans
}
