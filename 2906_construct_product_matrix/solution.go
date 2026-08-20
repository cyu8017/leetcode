// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

func constructProductMatrix(grid [][]int) [][]int {
	const mod = 12345
	m, n := len(grid), len(grid[0])
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
	}
	pref := 1
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			ans[i][j] = pref
			pref = pref * (grid[i][j] % mod) % mod
		}
	}
	suf := 1
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			ans[i][j] = ans[i][j] * suf % mod
			suf = suf * (grid[i][j] % mod) % mod
		}
	}
	return ans
}
