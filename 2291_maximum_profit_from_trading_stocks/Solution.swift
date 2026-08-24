// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

class Solution {
    func maximumProfit(_ present: [Int], _ future: [Int], _ budget: Int) -> Int {
        var dp = [Int](repeating: 0, count: budget + 1)
        for i in 0..<present.count {
            let profit = future[i] - present[i]
            if profit <= 0 { continue }
            let cost = present[i]
            if cost <= budget {
                for b in stride(from: budget, through: cost, by: -1) {
                    dp[b] = max(dp[b], dp[b - cost] + profit)
                }
            }
        }
        return dp[budget]
    }
}
