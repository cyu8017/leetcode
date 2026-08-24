// LeetCode 0562 - Longest Line of Consecutive One in Matrix
// https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

class Solution {
    func longestLine(_ mat: [[Int]]) -> Int {
        guard !mat.isEmpty, !mat[0].isEmpty else { return 0 }
        let rows = mat.count
        let cols = mat[0].count
        var dp = Array(repeating: Array(repeating: [0, 0, 0, 0], count: cols), count: rows)
        var best = 0
        for r in 0..<rows {
            for c in 0..<cols {
                if mat[r][c] == 0 { continue }
                dp[r][c][0] = (c > 0 ? dp[r][c - 1][0] : 0) + 1
                dp[r][c][1] = (r > 0 ? dp[r - 1][c][1] : 0) + 1
                dp[r][c][2] = (r > 0 && c > 0 ? dp[r - 1][c - 1][2] : 0) + 1
                dp[r][c][3] = (r > 0 && c + 1 < cols ? dp[r - 1][c + 1][3] : 0) + 1
                for d in 0..<4 {
                    best = max(best, dp[r][c][d])
                }
            }
        }
        return best
    }
}
