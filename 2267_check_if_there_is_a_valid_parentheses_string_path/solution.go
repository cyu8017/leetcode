// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

func hasValidPath(grid [][]byte) bool {
	m, n := len(grid), len(grid[0])
	if (m+n-1)%2 == 1 || grid[0][0] == ')' || grid[m-1][n-1] == '(' {
		return false
	}
	type key struct{ r, c, bal int }
	vis := map[key]bool{}
	var dfs func(r, c, bal int) bool
	dfs = func(r, c, bal int) bool {
		if r >= m || c >= n {
			return false
		}
		if grid[r][c] == '(' {
			bal++
		} else {
			bal--
		}
		if bal < 0 {
			return false
		}
		if r == m-1 && c == n-1 {
			return bal == 0
		}
		k := key{r, c, bal}
		if vis[k] {
			return false
		}
		vis[k] = true
		return dfs(r+1, c, bal) || dfs(r, c+1, bal)
	}
	return dfs(0, 0, 0)
}
