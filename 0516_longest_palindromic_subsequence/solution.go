// LeetCode 0516 - Longest Palindromic Subsequence
// https://leetcode.com/problems/longest-palindromic-subsequence/

func longestPalindromeSubseq(s string) int {
	length := len(s)
	dp := make([][]int, length)
	for index := range dp {
		dp[index] = make([]int, length)
	}
	for index := length - 1; index >= 0; index-- {
		dp[index][index] = 1
		for end := index + 1; end < length; end++ {
			if s[index] == s[end] {
				dp[index][end] = dp[index+1][end-1] + 2
			} else {
				dp[index][end] = max(dp[index+1][end], dp[index][end-1])
			}
		}
	}
	return dp[0][length-1]
}
