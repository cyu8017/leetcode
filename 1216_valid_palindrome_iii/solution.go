// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

func isValidPalindrome(s string, k int) bool {
	n := len(s)
	if n == 0 {
		return true
	}
	dp := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		previous := 0
		for j := i + 1; j < n; j++ {
			old := dp[j]
			if s[i] == s[j] {
				dp[j] = previous
			} else {
				dp[j] = 1 + dp[j]
				if 1+dp[j-1] < dp[j] {
					dp[j] = 1 + dp[j-1]
				}
			}
			previous = old
		}
	}
	return dp[n-1] <= k
}
