// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution {
    func maxProfit(_ prices: [Int], _ fee: Int) -> Int {
        var hold = -prices[0], cash = 0
        for i in 1..<prices.count {
            hold = max(hold, cash - prices[i])
            cash = max(cash, hold + prices[i] - fee)
        }
        return cash
    }
}
