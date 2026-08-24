// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

class Solution {
    func maxProfit(_ prices: [Int], _ strategy: [Int], _ k: Int) -> Int {
        let n = prices.count
        var s = Array(repeating: 0, count: n + 1)
        var t = Array(repeating: 0, count: n + 1)
        for i in 1...n {
            s[i] = s[i - 1] + prices[i - 1] * strategy[i - 1]
            t[i] = t[i - 1] + prices[i - 1]
        }
        var ans = s[n]
        if k <= n {
            for i in k...n {
                ans = max(ans, s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k / 2]))
            }
        }
        return ans
    }
}
