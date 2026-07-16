// LeetCode 0122 - Best Time to Buy and Sell Stock II
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var profit = 0
        for index in 1..<prices.count {
            profit += max(0, prices[index] - prices[index - 1])
        }
        return profit
    }
}