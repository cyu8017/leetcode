// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

class Solution {
    func minFallingPathSum(_ matrix: [[Int]]) -> Int {
        var dp = matrix[0]
        if matrix.count > 1 {
            for r in 1..<matrix.count {
                var ndp = Array(repeating: 0, count: dp.count)
                for c in 0..<dp.count {
                    var best = dp[c]
                    if c > 0 { best = min(best, dp[c - 1]) }
                    if c + 1 < dp.count { best = min(best, dp[c + 1]) }
                    ndp[c] = matrix[r][c] + best
                }
                dp = ndp
            }
        }
        return dp.min() ?? 0
    }
}
