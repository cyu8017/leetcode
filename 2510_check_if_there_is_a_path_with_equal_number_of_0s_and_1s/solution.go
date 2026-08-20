// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

func isThereAPath(grid [][]int) bool {
	m, n := len(grid), len(grid[0])
	if (m+n-1)%2 != 0 {
		return false
	}
	target := (m + n - 1) / 2
	type key struct{ r, c, bal int }
	memo := map[key]bool{}
	var dfs func(r, c, bal int) bool
	dfs = func(r, c, bal int) bool {
		if r >= m || c >= n {
			return false
		}
		bal += grid[r][c]
		if bal > target || bal+(m-1-r)+(n-1-c) < target {
			return false
		}
		if r == m-1 && c == n-1 {
			return bal == target
		}
		k := key{r, c, bal}
		if v, ok := memo[k]; ok {
			return v
		}
		ok := dfs(r+1, c, bal) || dfs(r, c+1, bal)
		memo[k] = ok
		return ok
	}
	return dfs(0, 0, 0)
}
