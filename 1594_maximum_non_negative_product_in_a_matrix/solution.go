// LeetCode 1594 - Maximum Non Negative Product in a Matrix
// https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

func maxProductPath(grid [][]int) int {
	const MOD = 1_000_000_007
	m, n := len(grid), len(grid[0])
	high := make([][]int64, m)
	low := make([][]int64, m)
	for i := range high {
		high[i] = make([]int64, n)
		low[i] = make([]int64, n)
	}
	high[0][0] = int64(grid[0][0])
	low[0][0] = int64(grid[0][0])
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if r == 0 && c == 0 {
				continue
			}
			values := []int64{}
			g := int64(grid[r][c])
			if r > 0 {
				values = append(values, high[r-1][c]*g, low[r-1][c]*g)
			}
			if c > 0 {
				values = append(values, high[r][c-1]*g, low[r][c-1]*g)
			}
			mx, mn := values[0], values[0]
			for _, v := range values[1:] {
				if v > mx {
					mx = v
				}
				if v < mn {
					mn = v
				}
			}
			high[r][c], low[r][c] = mx, mn
		}
	}
	if high[m-1][n-1] < 0 {
		return -1
	}
	return int(high[m-1][n-1] % MOD)
}
