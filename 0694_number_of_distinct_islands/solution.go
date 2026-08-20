// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

func numDistinctIslands(grid [][]int) int {
	if len(grid) == 0 {
		return 0
	}
	m, n := len(grid), len(grid[0])
	shapes := map[string]struct{}{}
	var dfs func(r, c, br, bc int, path *[][2]int)
	dfs = func(r, c, br, bc int, path *[][2]int) {
		if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 {
			return
		}
		grid[r][c] = 0
		*path = append(*path, [2]int{r - br, c - bc})
		dfs(r+1, c, br, bc, path)
		dfs(r-1, c, br, bc, path)
		dfs(r, c+1, br, bc, path)
		dfs(r, c-1, br, bc, path)
	}
	encode := func(path [][2]int) string {
		b := make([]byte, 0, len(path)*4)
		for _, p := range path {
			b = append(b, byte(p[0]+64), ',', byte(p[1]+64), ';')
		}
		return string(b)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				path := [][2]int{}
				dfs(i, j, i, j, &path)
				shapes[encode(path)] = struct{}{}
			}
		}
	}
	return len(shapes)
}
