// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

class Solution {
    func minXor(_ grid: [[Int]]) -> Int {
        let rows = grid.count, cols = grid[0].count
        var dp = Array(repeating: [Bool](repeating: false, count: 1024), count: cols)
        for row in 0..<rows {
            var left = [Bool](repeating: false, count: 1024)
            for col in 0..<cols {
                var next = [Bool](repeating: false, count: 1024)
                let value = grid[row][col]
                if row == 0 && col == 0 {
                    next[value] = true
                } else {
                    for xorv in 0..<1024 {
                        if dp[col][xorv] || left[xorv] { next[xorv ^ value] = true }
                    }
                }
                dp[col] = next
                left = next
            }
        }
        for xorv in 0..<1024 {
            if dp[cols - 1][xorv] { return xorv }
        }
        return -1
    }
}
