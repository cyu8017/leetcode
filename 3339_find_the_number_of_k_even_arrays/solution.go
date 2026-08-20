// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

func countOfArrays(n int, m int, k int) int {
	const mod = 1000000007
	even := m / 2
	odd := m - even
	// dp[i][j][parity] i length, j consecutive even pairs count
	dp := make([][][2]int, n+1)
	for i := range dp {
		dp[i] = make([][2]int, k+1)
	}
	dp[1][0][0] = odd
	dp[1][0][1] = even
	for i := 1; i < n; i++ {
		for j := 0; j <= k; j++ {
			// append odd
			dp[i+1][j][0] = (dp[i+1][j][0] + (dp[i][j][0]+dp[i][j][1])%mod*odd) % mod
			// append even after odd: no new pair
			dp[i+1][j][1] = (dp[i+1][j][1] + dp[i][j][0]*even) % mod
			// append even after even: new pair
			if j < k {
				dp[i+1][j+1][1] = (dp[i+1][j+1][1] + dp[i][j][1]*even) % mod
			}
		}
	}
	return (dp[n][k][0] + dp[n][k][1]) % mod
}
