// LeetCode 0664 - Strange Printer
// https://leetcode.com/problems/strange-printer/

func strangePrinter(s string) int {
	n := len(s)
	memo := make([][]int, n)
	for i := range memo {
		memo[i] = make([]int, n)
		for j := range memo[i] {
			memo[i][j] = -1
		}
	}
	var dfs func(i, j int) int
	dfs = func(i, j int) int {
		if i > j {
			return 0
		}
		if memo[i][j] != -1 {
			return memo[i][j]
		}
		ans := dfs(i+1, j) + 1
		for k := i + 1; k <= j; k++ {
			if s[k] == s[i] {
				cand := dfs(i, k-1) + dfs(k+1, j)
				if cand < ans {
					ans = cand
				}
			}
		}
		memo[i][j] = ans
		return ans
	}
	return dfs(0, n-1)
}
