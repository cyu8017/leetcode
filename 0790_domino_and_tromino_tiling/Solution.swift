// LeetCode 0790 - Domino and Tromino Tiling
// https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution {
    func numTilings(_ n: Int) -> Int {
        let mod = 1_000_000_007
        if n == 1 { return 1 }
        if n == 2 { return 2 }
        var dp = Array(repeating: 0, count: n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        if n >= 4 {
            for i in 4...n {
                dp[i] = (2 * dp[i - 1] + dp[i - 3]) % mod
            }
        }
        return dp[n]
    }
}
