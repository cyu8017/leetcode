// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/

class Solution {
    func waysToReachTarget(_ target: Int, _ types: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        var dp = [Int](repeating: 0, count: target + 1)
        dp[0] = 1
        for t in types {
            let count = t[0], marks = t[1]
            for s in stride(from: target, through: 0, by: -1) {
                var k = 1
                while k <= count && s - k * marks >= 0 {
                    dp[s] = (dp[s] + dp[s - k * marks]) % MOD
                    k += 1
                }
            }
        }
        return dp[target]
    }
}
