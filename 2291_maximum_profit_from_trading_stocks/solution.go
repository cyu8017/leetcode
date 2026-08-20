// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

func maximumProfit(present []int, future []int, budget int) int {
	n := len(present)
	dp := make([]int, budget+1)
	for i := 0; i < n; i++ {
		profit := future[i] - present[i]
		if profit <= 0 {
			continue
		}
		cost := present[i]
		for b := budget; b >= cost; b-- {
			if dp[b-cost]+profit > dp[b] {
				dp[b] = dp[b-cost] + profit
			}
		}
	}
	return dp[budget]
}
