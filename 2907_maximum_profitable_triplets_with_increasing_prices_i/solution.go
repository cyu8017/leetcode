// LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

func maxProfit(prices []int, profits []int) int {
	n := len(prices)
	ans := -1
	for j := 0; j < n; j++ {
		bestL, bestR := -1, -1
		for i := 0; i < j; i++ {
			if prices[i] < prices[j] && profits[i] > bestL {
				bestL = profits[i]
			}
		}
		for k := j + 1; k < n; k++ {
			if prices[k] > prices[j] && profits[k] > bestR {
				bestR = profits[k]
			}
		}
		if bestL >= 0 && bestR >= 0 {
			cand := bestL + profits[j] + bestR
			if cand > ans {
				ans = cand
			}
		}
	}
	return ans
}
