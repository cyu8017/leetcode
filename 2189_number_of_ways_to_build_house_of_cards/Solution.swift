// LeetCode 2189 - Number of Ways to Build House of Cards
// https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

class Solution {
    func houseOfCards(_ n: Int) -> Int {
        var dp = [Int](repeating: 0, count: n + 1)
        dp[0] = 1
        var k = 1
        while 3 * k - 1 <= n {
            let cost = 3 * k - 1
            for j in stride(from: n, through: cost, by: -1) { dp[j] += dp[j - cost] }
            k += 1
        }
        return dp[n]
    }
}
