// LeetCode 2132 - Stamping the Grid
// https://leetcode.com/problems/stamping-the-grid/

func possibleToStamp(grid [][]int, stampHeight int, stampWidth int) bool {
	m, n := len(grid), len(grid[0])
	pref := make([][]int, m+1)
	for i := range pref {
		pref[i] = make([]int, n+1)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			pref[i+1][j+1] = pref[i+1][j] + pref[i][j+1] - pref[i][j] + grid[i][j]
		}
	}
	sum := func(r1, c1, r2, c2 int) int {
		return pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]
	}
	diff := make([][]int, m+1)
	for i := range diff {
		diff[i] = make([]int, n+1)
	}
	for i := 0; i+stampHeight-1 < m; i++ {
		for j := 0; j+stampWidth-1 < n; j++ {
			if sum(i, j, i+stampHeight-1, j+stampWidth-1) == 0 {
				diff[i][j]++
				diff[i][j+stampWidth]--
				diff[i+stampHeight][j]--
				diff[i+stampHeight][j+stampWidth]++
			}
		}
	}
	cur := make([][]int, m)
	for i := 0; i < m; i++ {
		cur[i] = make([]int, n)
		for j := 0; j < n; j++ {
			v := diff[i][j]
			if i > 0 {
				v += cur[i-1][j]
			}
			if j > 0 {
				v += cur[i][j-1]
			}
			if i > 0 && j > 0 {
				v -= cur[i-1][j-1]
			}
			cur[i][j] = v
			if grid[i][j] == 0 && v == 0 {
				return false
			}
		}
	}
	return true
}
