// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

func maxProfit(n int, edges [][]int, score []int) int {
	need := make([]int, n)
	dp := make([]int, 1<<n)
	for i := range dp {
		dp[i] = -1
	}
	dp[0] = 0
	for _, e := range edges {
		need[e[1]] |= 1 << e[0]
	}
	pop := func(x int) int {
		c := 0
		for x > 0 {
			c += x & 1
			x >>= 1
		}
		return c
	}
	for mask := 0; mask < 1<<n; mask++ {
		if dp[mask] < 0 {
			continue
		}
		pos := pop(mask) + 1
		for i := 0; i < n; i++ {
			if mask>>i&1 == 1 {
				continue
			}
			if mask&need[i] == need[i] {
				nm := mask | 1<<i
				v := dp[mask] + score[i]*pos
				if v > dp[nm] {
					dp[nm] = v
				}
			}
		}
	}
	return dp[(1<<n)-1]
}
