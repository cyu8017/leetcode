// LeetCode 0651 - 4 Keys Keyboard
// https://leetcode.com/problems/4-keys-keyboard/

func maxA(n int) int {
	dp := make([]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = i
	}
	for i := 1; i <= n; i++ {
		for j := 0; j < i-2; j++ {
			cand := dp[j] * (i - j - 1)
			if cand > dp[i] {
				dp[i] = cand
			}
		}
	}
	return dp[n]
}
