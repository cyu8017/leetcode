// LeetCode 0322 - Coin Change
// https://leetcode.com/problems/coin-change/

class Solution {
    func coinChange(_ coins: [Int], _ amount: Int) -> Int {
        let maxValue = amount + 1
        var dp = Array(repeating: maxValue, count: amount + 1)
        dp[0] = 0
        for coin in coins {
            if coin > amount {
                continue
            }
            for value in coin...amount {
                dp[value] = min(dp[value], dp[value - coin] + 1)
            }
        }
        return dp[amount] == maxValue ? -1 : dp[amount]
    }
}
