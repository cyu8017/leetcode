// LeetCode 0518 - Coin Change II
// https://leetcode.com/problems/coin-change-ii/

class Solution {
    func change(_ amount: Int, _ coins: [Int]) -> Int {
        var dp = Array(repeating: 0, count: amount + 1)
        dp[0] = 1

        for coin in coins {
            for value in coin...amount {
                dp[value] += dp[value - coin]
            }
        }

        return dp[amount]
    }
}
