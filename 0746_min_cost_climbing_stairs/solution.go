// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

func minCostClimbingStairs(cost []int) int {
	a, b := 0, 0
	for i := len(cost) - 1; i >= 0; i-- {
		a, b = cost[i]+min(a, b), a
	}
	return min(a, b)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
