// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

func deleteString(s string) int {
	n := len(s)
	lcp := make([][]int, n+1)
	for i := range lcp {
		lcp[i] = make([]int, n+1)
	}
	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if s[i] == s[j] {
				lcp[i][j] = lcp[i+1][j+1] + 1
			}
		}
	}
	dp := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		dp[i] = 1
		for len_ := 1; i+2*len_ <= n; len_++ {
			if lcp[i][i+len_] >= len_ {
				if 1+dp[i+len_] > dp[i] {
					dp[i] = 1 + dp[i+len_]
				}
			}
		}
	}
	return dp[0]
}
