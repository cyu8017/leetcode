// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

func beautifulPartitions(s string, k int, minLength int) int {
	const mod = 1000000007
	isPrime := func(c byte) bool {
		return c == '2' || c == '3' || c == '5' || c == '7'
	}
	n := len(s)
	if !isPrime(s[0]) || isPrime(s[n-1]) {
		return 0
	}
	dp := make([][]int, k+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	dp[0][0] = 1
	for p := 1; p <= k; p++ {
		pref := 0
		j := 0
		for i := 1; i <= n; i++ {
			for j <= i-minLength {
				if j == 0 || (isPrime(s[j]) && !isPrime(s[j-1])) {
					pref = (pref + dp[p-1][j]) % mod
				}
				j++
			}
			if !isPrime(s[i-1]) {
				dp[p][i] = pref
			}
		}
	}
	return dp[k][n]
}
