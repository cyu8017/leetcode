// LeetCode 2969 - Minimum Number of Coins for Fruits II
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

class Solution {
    func minimumCoins(_ prices: [Int]) -> Int {
        let n = prices.count
        var dp = Array(repeating: 1 << 30, count: n + 1)
        dp[0] = 0
        for i in 1...n {
            var j = i
            while j <= n && j <= 2 * i {
                dp[j] = min(dp[j], dp[i - 1] + prices[i - 1])
                j += 1
            }
        }
        return dp[n]
    }
}
