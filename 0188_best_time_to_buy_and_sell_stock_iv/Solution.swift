// LeetCode 0188 - Best Time to Buy and Sell Stock IV
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

class Solution {
    func maxProfit(_ k: Int, _ prices: [Int]) -> Int {
        let n = prices.count
        if n == 0 || k == 0 {
            return 0
        }
        if k >= n / 2 {
            var profit = 0
            for index in 1..<n {
                profit += max(prices[index] - prices[index - 1], 0)
            }
            return profit
        }

        var buy = Array(repeating: Int.max, count: k + 1)
        var sell = Array(repeating: 0, count: k + 1)
        for price in prices {
            for transaction in 1...k {
                buy[transaction] = min(buy[transaction], price - sell[transaction - 1])
                sell[transaction] = max(sell[transaction], price - buy[transaction])
            }
        }
        return sell[k]
    }
}