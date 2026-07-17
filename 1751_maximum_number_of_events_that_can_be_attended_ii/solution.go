// LeetCode 1751 - Maximum Number of Events That Can Be Attended II
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

import "sort"

func maxValue(events [][]int, k int) int {
	sort.Slice(events, func(a, b int) bool {
		if events[a][0] != events[b][0] {
			return events[a][0] < events[b][0]
		}
		if events[a][1] != events[b][1] {
			return events[a][1] < events[b][1]
		}
		return events[a][2] < events[b][2]
	})
	n := len(events)
	starts := make([]int, n)
	for i, e := range events {
		starts[i] = e[0]
	}

	dp := make([][]int, k+1)
	for remain := range dp {
		dp[remain] = make([]int, n+1)
	}
	for i := n - 1; i >= 0; i-- {
		j := sort.SearchInts(starts, events[i][1]+1)
		for remain := 1; remain <= k; remain++ {
			skip := dp[remain][i+1]
			take := events[i][2] + dp[remain-1][j]
			if take > skip {
				dp[remain][i] = take
			} else {
				dp[remain][i] = skip
			}
		}
	}
	return dp[k][0]
}
