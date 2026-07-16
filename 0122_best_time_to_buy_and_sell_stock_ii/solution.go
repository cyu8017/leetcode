// LeetCode 0122 - Best Time to Buy and Sell Stock II
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

func maxProfit(prices []int) int { profit := 0; for i := 1; i < len(prices); i++ { if prices[i] > prices[i-1] { profit += prices[i]-prices[i-1] } }; return profit }