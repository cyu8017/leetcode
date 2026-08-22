// LeetCode 3857 - Minimum Cost To Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

func minCost(n int) int {
	return n * (n - 1) / 2
}
