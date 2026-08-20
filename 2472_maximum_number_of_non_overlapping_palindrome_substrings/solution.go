// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

func maxPalindromes(s string, k int) int {
	n := len(s)
	isPal := make([][]bool, n)
	for i := range isPal {
		isPal[i] = make([]bool, n)
		isPal[i][i] = true
	}
	for i := 0; i+1 < n; i++ {
		isPal[i][i+1] = s[i] == s[i+1]
	}
	for length := 3; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			isPal[i][j] = s[i] == s[j] && isPal[i+1][j-1]
		}
	}
	dp := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		dp[i] = dp[i+1]
		for j := i + k - 1; j < n; j++ {
			if isPal[i][j] {
				if 1+dp[j+1] > dp[i] {
					dp[i] = 1 + dp[j+1]
				}
			}
		}
	}
	return dp[0]
}
