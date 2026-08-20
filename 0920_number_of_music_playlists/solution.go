// LeetCode 0920 - Number of Music Playlists
// https://leetcode.com/problems/number-of-music-playlists/

func numMusicPlaylists(n int, goal int, k int) int {
	const MOD = 1000000007
	dp := make([][]int, goal+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	dp[0][0] = 1
	for i := 1; i <= goal; i++ {
		lim := i
		if lim > n {
			lim = n
		}
		for j := 1; j <= lim; j++ {
			dp[i][j] = dp[i-1][j-1] * (n - j + 1) % MOD
			if j > k {
				dp[i][j] = (dp[i][j] + dp[i-1][j]*(j-k)) % MOD
			}
		}
	}
	return dp[goal][n]
}
