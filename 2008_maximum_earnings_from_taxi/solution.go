// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

import "sort"

func maxTaxiEarnings(n int, rides [][]int) int64 {
	sort.Slice(rides, func(i, j int) bool { return rides[i][1] < rides[j][1] })
	m := len(rides)
	ends := make([]int, m)
	for i, r := range rides {
		ends[i] = r[1]
	}
	dp := make([]int64, m+1)
	for i, r := range rides {
		start, end, tip := r[0], r[1], r[2]
		earn := int64(end - start + tip)
		j := sort.Search(m, func(k int) bool { return ends[k] > start })
		cand := earn + dp[j]
		dp[i+1] = dp[i]
		if cand > dp[i+1] {
			dp[i+1] = cand
		}
	}
	return dp[m]
}
