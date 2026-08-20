// LeetCode 0903 - Valid Permutations for DI Sequence
// https://leetcode.com/problems/valid-permutations-for-di-sequence/

func numPermsDISequence(s string) int {
	const MOD = 1000000007
	n := len(s)
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = 1
	}
	for i := 1; i <= n; i++ {
		newDp := make([]int, n+1)
		if s[i-1] == 'I' {
			postfix := 0
			for j := n - i; j >= 0; j-- {
				postfix = (postfix + dp[j+1]) % MOD
				newDp[j] = postfix
			}
		} else {
			prefix := 0
			for j := 0; j <= n-i; j++ {
				prefix = (prefix + dp[j]) % MOD
				newDp[j] = prefix
			}
		}
		dp = newDp
	}
	return dp[0]
}
