// LeetCode 0221 - Maximal Square
// https://leetcode.com/problems/maximal-square/

class Solution {
    func maximalSquare(_ matrix: [[Character]]) -> Int {
        if matrix.isEmpty {
            return 0
        }
        let rows = matrix.count
        let cols = matrix[0].count
        var dp = Array(repeating: 0, count: cols + 1)
        var maxSide = 0
        var prev = 0
        for row in 1...rows {
            for col in 1...cols {
                let temp = dp[col]
                if matrix[row - 1][col - 1] == "1" {
                    dp[col] = min(dp[col], dp[col - 1], prev) + 1
                    maxSide = max(maxSide, dp[col])
                } else {
                    dp[col] = 0
                }
                prev = temp
            }
        }
        return maxSide * maxSide
    }
}
