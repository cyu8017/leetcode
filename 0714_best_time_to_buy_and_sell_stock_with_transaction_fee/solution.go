// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

func maxProfit(prices []int, fee int) int {
	hold := -prices[0]
	cash := 0
	for _, price := range prices[1:] {
		if cash-price > hold {
			hold = cash - price
		}
		if hold+price-fee > cash {
			cash = hold + price - fee
		}
	}
	return cash
}
