// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

func longestCommonSubsequence(text1 string, text2 string) int {
	m, n := len(text1), len(text2)
	dp := make([]int, n+1)
	for i := 1; i <= m; i++ {
		prev := 0
		for j := 1; j <= n; j++ {
			cur := dp[j]
			if text1[i-1] == text2[j-1] {
				dp[j] = prev + 1
			} else if dp[j-1] > dp[j] {
				dp[j] = dp[j-1]
			}
			prev = cur
		}
	}
	return dp[n]
}
