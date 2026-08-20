// LeetCode 0730 - Count Different Palindromic Subsequences
// https://leetcode.com/problems/count-different-palindromic-subsequences/

func countPalindromicSubsequences(s string) int {
	const mod = 1000000007
	n := len(s)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
		dp[i][i] = 1
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			if s[i] != s[j] {
				dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
			} else {
				left, right := i+1, j-1
				for left <= right && s[left] != s[i] {
					left++
				}
				for left <= right && s[right] != s[i] {
					right--
				}
				if left > right {
					dp[i][j] = dp[i+1][j-1]*2 + 2
				} else if left == right {
					dp[i][j] = dp[i+1][j-1]*2 + 1
				} else {
					dp[i][j] = dp[i+1][j-1]*2 - dp[left+1][right-1]
				}
			}
			dp[i][j] = (dp[i][j]%mod + mod) % mod
		}
	}
	return dp[0][n-1]
}
