// LeetCode 1595 - Minimum Cost to Connect Two Groups of Points
// https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

func connectTwoGroups(cost [][]int) int {
	m, n := len(cost), len(cost[0])
	full := 1 << n
	const inf = 1_000_000_000
	dp := make([]int, full)
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	for _, row := range cost {
		nxt := make([]int, full)
		for i := range nxt {
			nxt[i] = inf
		}
		for mask := 0; mask < full; mask++ {
			if dp[mask] >= inf {
				continue
			}
			for j, value := range row {
				newMask := mask | (1 << j)
				if dp[mask]+value < nxt[newMask] {
					nxt[newMask] = dp[mask] + value
				}
				if nxt[mask]+value < nxt[newMask] {
					nxt[newMask] = nxt[mask] + value
				}
			}
		}
		dp = nxt
	}
	minimum := make([]int, n)
	for j := 0; j < n; j++ {
		minimum[j] = cost[0][j]
		for i := 1; i < m; i++ {
			if cost[i][j] < minimum[j] {
				minimum[j] = cost[i][j]
			}
		}
	}
	ans := inf
	for mask := 0; mask < full; mask++ {
		extra := 0
		for j := 0; j < n; j++ {
			if mask&(1<<j) == 0 {
				extra += minimum[j]
			}
		}
		if dp[mask]+extra < ans {
			ans = dp[mask] + extra
		}
	}
	return ans
}
