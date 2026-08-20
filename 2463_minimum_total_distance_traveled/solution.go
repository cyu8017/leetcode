// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

import "sort"

func minimumTotalDistance(robot []int, factory [][]int) int64 {
	sort.Ints(robot)
	sort.Slice(factory, func(i, j int) bool { return factory[i][0] < factory[j][0] })
	m := len(robot)
	pos := []int{}
	for _, f := range factory {
		for c := 0; c < f[1]; c++ {
			pos = append(pos, f[0])
		}
	}
	n := len(pos)
	dp := make([][]int64, m+1)
	for i := range dp {
		dp[i] = make([]int64, n+1)
		for j := range dp[i] {
			dp[i][j] = 1 << 60
		}
	}
	for j := 0; j <= n; j++ {
		dp[0][j] = 0
	}
	for i := 1; i <= m; i++ {
		for j := i; j <= n; j++ {
			dp[i][j] = dp[i][j-1]
			diff := int64(robot[i-1] - pos[j-1])
			if diff < 0 {
				diff = -diff
			}
			if dp[i-1][j-1]+diff < dp[i][j] {
				dp[i][j] = dp[i-1][j-1] + diff
			}
		}
	}
	return dp[m][n]
}
