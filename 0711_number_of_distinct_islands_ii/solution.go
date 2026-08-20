// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

import (
	"fmt"
	"sort"
)

func numDistinctIslands2(grid [][]int) int {
	if len(grid) == 0 {
		return 0
	}
	m, n := len(grid), len(grid[0])
	shapes := map[string]struct{}{}
	var dfs func(r, c int, cells *[][2]int)
	dfs = func(r, c int, cells *[][2]int) {
		if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 {
			return
		}
		grid[r][c] = 0
		*cells = append(*cells, [2]int{r, c})
		dfs(r+1, c, cells)
		dfs(r-1, c, cells)
		dfs(r, c+1, cells)
		dfs(r, c-1, cells)
	}
	transforms := []func(x, y int) (int, int){
		func(x, y int) (int, int) { return x, y },
		func(x, y int) (int, int) { return x, -y },
		func(x, y int) (int, int) { return -x, y },
		func(x, y int) (int, int) { return -x, -y },
		func(x, y int) (int, int) { return y, x },
		func(x, y int) (int, int) { return y, -x },
		func(x, y int) (int, int) { return -y, x },
		func(x, y int) (int, int) { return -y, -x },
	}
	canonical := func(cells [][2]int) string {
		norms := []string{}
		for _, transform := range transforms {
			pts := make([][2]int, len(cells))
			minX, minY := 1<<30, 1<<30
			for i, cell := range cells {
				x, y := transform(cell[0], cell[1])
				pts[i] = [2]int{x, y}
				if x < minX {
					minX = x
				}
				if y < minY {
					minY = y
				}
			}
			for i := range pts {
				pts[i][0] -= minX
				pts[i][1] -= minY
			}
			sort.Slice(pts, func(i, j int) bool {
				if pts[i][0] == pts[j][0] {
					return pts[i][1] < pts[j][1]
				}
				return pts[i][0] < pts[j][0]
			})
			norms = append(norms, fmt.Sprint(pts))
		}
		sort.Strings(norms)
		return norms[0]
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				cells := [][2]int{}
				dfs(i, j, &cells)
				shapes[canonical(cells)] = struct{}{}
			}
		}
	}
	return len(shapes)
}
