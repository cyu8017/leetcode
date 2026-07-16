// LeetCode 0123 - Best Time to Buy and Sell Stock III
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

func maxProfit(prices []int) int { b1,b2,s1,s2 := 1<<31-1,1<<31-1,0,0; for _, p := range prices { if p < b1 { b1=p }; if p-b1 > s1 { s1=p-b1 }; if p-s1 < b2 { b2=p-s1 }; if p-b2 > s2 { s2=p-b2 } }; return s2 }