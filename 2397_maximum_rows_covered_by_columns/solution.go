// LeetCode 2397 - Maximum Rows Covered by Columns
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

func maximumRows(matrix [][]int, numSelect int) int {
	m, n := len(matrix), len(matrix[0])
	ans := 0
	var dfs func(int, int, int)
	dfs = func(col, chosen, mask int) {
		if chosen == numSelect {
			covered := 0
			for i := 0; i < m; i++ {
				ok := true
				for j := 0; j < n; j++ {
					if matrix[i][j] == 1 && (mask>>j)&1 == 0 {
						ok = false
						break
					}
				}
				if ok {
					covered++
				}
			}
			if covered > ans {
				ans = covered
			}
			return
		}
		if col == n {
			return
		}
		dfs(col+1, chosen+1, mask|(1<<col))
		dfs(col+1, chosen, mask)
	}
	dfs(0, 0, 0)
	return ans
}
