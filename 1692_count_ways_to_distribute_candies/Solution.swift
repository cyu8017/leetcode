// LeetCode 1692 - Count Ways to Distribute Candies
// https://leetcode.com/problems/count-ways-to-distribute-candies/

class Solution {
    func waysToDistribute(_ n: Int, _ k: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = Array(repeating: 0, count: k + 1)
        dp[0] = 1
        for i in 1...n {
            for j in stride(from: min(i, k), through: 1, by: -1) {
                dp[j] = (dp[j - 1] + j * dp[j]) % MOD
            }
            dp[0] = 0
        }
        return dp[k]
    }
}
