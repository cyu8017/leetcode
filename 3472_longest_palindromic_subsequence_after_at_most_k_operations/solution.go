// LeetCode 3472 - Longest Palindromic Subsequence After At Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

func longestPalindromicSubsequence(s string, k int) int {
	n := len(s)
	// dp[i][j][ops]
	dp := make([][][]int, n)
	for i := range dp {
		dp[i] = make([][]int, n)
		for j := range dp[i] {
			dp[i][j] = make([]int, k+1)
			for t := 0; t <= k; t++ {
				dp[i][j][t] = -1
			}
		}
	}
	var dfs func(i, j, ops int) int
	dfs = func(i, j, ops int) int {
		if i > j {
			return 0
		}
		if i == j {
			return 1
		}
		if dp[i][j][ops] != -1 {
			return dp[i][j][ops]
		}
		best := dfs(i+1, j, ops)
		if v := dfs(i, j-1, ops); v > best {
			best = v
		}
		cost := distCirc(s[i], s[j])
		if cost <= ops {
			v := 2 + dfs(i+1, j-1, ops-cost)
			if v > best {
				best = v
			}
		}
		dp[i][j][ops] = best
		return best
	}
	return dfs(0, n-1, k)
}

func distCirc(a, b byte) int {
	d := int(a) - int(b)
	if d < 0 {
		d = -d
	}
	if 26-d < d {
		return 26 - d
	}
	return d
}
