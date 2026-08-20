// LeetCode 3958 - Minimum Cost To Split Into Ones Ii
// https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/

func minCost(n int) int64 {
	return int64(n * (n - 1) / 2)
}
