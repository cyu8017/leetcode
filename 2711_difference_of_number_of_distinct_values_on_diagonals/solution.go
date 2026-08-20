// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/


func differenceOfDistinctValues(grid [][]int) [][]int {
	m, n := len(grid), len(grid[0])
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			tl := map[int]bool{}
			for x, y := i-1, j-1; x >= 0 && y >= 0; x, y = x-1, y-1 {
				tl[grid[x][y]] = true
			}
			br := map[int]bool{}
			for x, y := i+1, j+1; x < m && y < n; x, y = x+1, y+1 {
				br[grid[x][y]] = true
			}
			d := len(tl) - len(br)
			if d < 0 {
				d = -d
			}
			ans[i][j] = d
		}
	}
	return ans
}
