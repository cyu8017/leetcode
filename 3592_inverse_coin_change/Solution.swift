// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

class Solution {
    func findCoins(_ numWays: [Int]) -> [Int] {
        let n = numWays.count
        var dp = Array(repeating: 0, count: n + 1)
        var coins = [Int]()
        dp[0] = 1
        for amt in 1...n {
            let ways = numWays[amt - 1]
            if dp[amt] == ways { continue }
            if dp[amt] + 1 == ways {
                coins.append(amt)
                for x in amt...n { dp[x] += dp[x - amt] }
                if dp[amt] != ways { return [] }
                continue
            }
            return []
        }
        return coins
    }
}
