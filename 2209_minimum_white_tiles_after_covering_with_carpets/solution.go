// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

func minimumWhiteTiles(floor string, numCarpets int, carpetLen int) int {
	n := len(floor)
	pref := make([]int, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i]
		if floor[i] == '1' {
			pref[i+1]++
		}
	}
	dp := make([][]int, numCarpets+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
		for j := range dp[i] {
			dp[i][j] = 1 << 30
		}
	}
	dp[0][0] = 0
	for j := 1; j <= n; j++ {
		dp[0][j] = dp[0][j-1]
		if floor[j-1] == '1' {
			dp[0][j]++
		}
	}
	for c := 1; c <= numCarpets; c++ {
		dp[c][0] = 0
		for j := 1; j <= n; j++ {
			// skip
			dp[c][j] = dp[c][j-1]
			if floor[j-1] == '1' {
				dp[c][j]++
			}
			// cover ending at j
			start := j - carpetLen
			if start < 0 {
				start = 0
			}
			cand := dp[c-1][start]
			if cand < dp[c][j] {
				dp[c][j] = cand
			}
		}
	}
	return dp[numCarpets][n]
}
