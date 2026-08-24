// LeetCode 3573 - Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

class Solution {
    func maximumProfit(_ prices: [Int], _ k: Int) -> Int {
        let n = prices.count
        var f = Array(repeating: Array(repeating: [0, 0, 0], count: k + 1), count: n)
        if k >= 1 {
            for j in 1...k {
                f[0][j][1] = -prices[0]
                f[0][j][2] = prices[0]
            }
        }
        if n > 1 {
            for i in 1..<n {
                if k >= 1 {
                    for j in 1...k {
                        f[i][j][0] = max(f[i - 1][j][0], max(f[i - 1][j][1] + prices[i], f[i - 1][j][2] - prices[i]))
                        f[i][j][1] = max(f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i])
                        f[i][j][2] = max(f[i - 1][j][2], f[i - 1][j - 1][0] + prices[i])
                    }
                }
            }
        }
        return f[n - 1][k][0]
    }
}
