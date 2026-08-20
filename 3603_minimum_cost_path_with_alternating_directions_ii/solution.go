// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

func minCost(m int, n int, waitCost [][]int) int64 {
	dp := make([][]int64, m)
	for i := range dp {
		dp[i] = make([]int64, n)
		for j := range dp[i] {
			dp[i][j] = 1 << 62
		}
	}
	entry := func(i, j int) int64 { return int64(i+1) * int64(j+1) }
	dp[0][0] = entry(0, 0)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				continue
			}
			if i > 0 {
				cand := dp[i-1][j] + entry(i, j)
				if !(i-1 == 0 && j == 0) {
					cand += int64(waitCost[i-1][j])
				}
				if cand < dp[i][j] {
					dp[i][j] = cand
				}
			}
			if j > 0 {
				cand := dp[i][j-1] + entry(i, j)
				if !(i == 0 && j-1 == 0) {
					cand += int64(waitCost[i][j-1])
				}
				if cand < dp[i][j] {
					dp[i][j] = cand
				}
			}
		}
	}
	return dp[m-1][n-1]
}
