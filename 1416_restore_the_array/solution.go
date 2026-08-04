// LeetCode 1416 - Restore The Array
// https://leetcode.com/problems/restore-the-array/

func numberOfArrays(s string, k int) int {
	const mod = 1000000007
	n := len(s)
	dp := make([]int, n+1)
	dp[n] = 1
	for i := n - 1; i >= 0; i-- {
		if s[i] == '0' {
			continue
		}
		value := 0
		for j := i; j < n; j++ {
			value = value*10 + int(s[j]-'0')
			if value > k {
				break
			}
			dp[i] = (dp[i] + dp[j+1]) % mod
		}
	}
	return dp[0]
}
