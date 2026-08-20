// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

func mincostTickets(days []int, costs []int) int {
	dayset := map[int]bool{}
	for _, d := range days {
		dayset[d] = true
	}
	last := days[len(days)-1]
	dp := make([]int, last+1)
	min3 := func(a, b, c int) int {
		if a > b {
			a = b
		}
		if a > c {
			a = c
		}
		return a
	}
	for d := 1; d <= last; d++ {
		if !dayset[d] {
			dp[d] = dp[d-1]
		} else {
			d7, d30 := d-7, d-30
			if d7 < 0 {
				d7 = 0
			}
			if d30 < 0 {
				d30 = 0
			}
			dp[d] = min3(dp[d-1]+costs[0], dp[d7]+costs[1], dp[d30]+costs[2])
		}
	}
	return dp[last]
}
