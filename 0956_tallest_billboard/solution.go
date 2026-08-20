// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

func tallestBillboard(rods []int) int {
	dp := map[int]int{0: 0}
	for _, rod := range rods {
		cur := make(map[int]int, len(dp))
		for k, v := range dp {
			cur[k] = v
		}
		for diff, taller := range cur {
			nd1 := diff + rod
			if v, ok := dp[nd1]; !ok || taller+rod > v {
				dp[nd1] = taller + rod
			}
			nd := diff - rod
			if nd < 0 {
				nd = -nd
			}
			var newTaller int
			if diff >= rod {
				newTaller = taller
			} else {
				newTaller = taller - diff + rod
			}
			if v, ok := dp[nd]; !ok || newTaller > v {
				dp[nd] = newTaller
			}
		}
	}
	return dp[0]
}
