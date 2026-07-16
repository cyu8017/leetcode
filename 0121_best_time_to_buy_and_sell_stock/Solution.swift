// LeetCode 0121 - Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var minimum = Int.max
        var profit = 0
        for price in prices {
            minimum = min(minimum, price)
            profit = max(profit, price - minimum)
        }
        return profit
    }
}