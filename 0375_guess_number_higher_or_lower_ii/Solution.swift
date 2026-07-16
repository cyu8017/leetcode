// LeetCode 0375 - Guess Number Higher or Lower II
// https://leetcode.com/problems/guess-number-higher-or-lower-ii/

class Solution {
    func getMoneyAmount(_ n: Int) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: n + 2), count: n + 2)

        for length in 2...n {
            for left in 1...(n - length + 1) {
                let right = left + length - 1
                dp[left][right] = Int.max
                for guess in left..<right {
                    let cost = guess + max(dp[left][guess - 1], dp[guess + 1][right])
                    dp[left][right] = min(dp[left][right], cost)
                }
            }
        }

        return dp[1][n]
    }
}
