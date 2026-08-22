// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

func minCuttingCost(n int, m int, k int) int64 {
	x := max(n, m)
	if x <= k {
		return 0
	}
	return int64(k * (x - k))
}
