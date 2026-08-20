// LeetCode 2338 - Count the Number of Ideal Arrays
// https://leetcode.com/problems/count-the-number-of-ideal-arrays/

func idealArrays(n int, maxValue int) int {
	const mod = 1000000007
	maxLen := 14
	comb := make([][]int, n+1)
	for i := range comb {
		comb[i] = make([]int, maxLen+1)
	}
	for i := 0; i <= n; i++ {
		comb[i][0] = 1
		for j := 1; j <= maxLen && j <= i; j++ {
			comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % mod
		}
	}
	dp := make([][]int, maxValue+1)
	for i := range dp {
		dp[i] = make([]int, maxLen+1)
	}
	for i := 1; i <= maxValue; i++ {
		dp[i][1] = 1
	}
	for len_ := 2; len_ <= maxLen; len_++ {
		for v := 1; v <= maxValue; v++ {
			for m := 2 * v; m <= maxValue; m += v {
				dp[m][len_] = (dp[m][len_] + dp[v][len_-1]) % mod
			}
		}
	}
	ans := 0
	for v := 1; v <= maxValue; v++ {
		for len_ := 1; len_ <= maxLen && len_ <= n; len_++ {
			ans = (ans + int(int64(dp[v][len_])*int64(comb[n-1][len_-1])%mod)) % mod
		}
	}
	return ans
}
