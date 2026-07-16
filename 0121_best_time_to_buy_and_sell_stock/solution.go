// LeetCode 0121 - Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

func maxProfit(prices []int) int { low, best := 1<<31-1, 0; for _, p := range prices { if p < low { low = p }; if p-low > best { best = p-low } }; return best }