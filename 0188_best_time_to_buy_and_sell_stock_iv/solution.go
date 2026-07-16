// LeetCode 0188 - Best Time to Buy and Sell Stock IV
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

func maxProfit(k int, prices []int) int {
	if len(prices) == 0 || k == 0 {
		return 0
	}
	if k >= len(prices)/2 {
		profit := 0
		for i := 1; i < len(prices); i++ {
			if prices[i] > prices[i-1] {
				profit += prices[i] - prices[i-1]
			}
		}
		return profit
	}

	buy := make([]int, k+1)
	sell := make([]int, k+1)
	for transaction := 1; transaction <= k; transaction++ {
		buy[transaction] = int(^uint(0) >> 1)
	}
	for _, price := range prices {
		for transaction := 1; transaction <= k; transaction++ {
			candidateBuy := price - sell[transaction-1]
			if candidateBuy < buy[transaction] {
				buy[transaction] = candidateBuy
			}
			candidateSell := price - buy[transaction]
			if candidateSell > sell[transaction] {
				sell[transaction] = candidateSell
			}
		}
	}
	return sell[k]
}