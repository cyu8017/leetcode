// LeetCode 1312 - Minimum Insertion Steps to Make a String Palindrome
// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

func minInsertions(s string) int {
	n := len(s)
	dp := make([]int, n)
	for left := n - 2; left >= 0; left-- {
		diagonal := 0
		for right := left + 1; right < n; right++ {
			old := dp[right]
			if s[left] == s[right] {
				dp[right] = diagonal
			} else {
				a, b := dp[right], dp[right-1]
				if a < b {
					dp[right] = 1 + a
				} else {
					dp[right] = 1 + b
				}
			}
			diagonal = old
		}
	}
	if n == 0 {
		return 0
	}
	return dp[n-1]
}
