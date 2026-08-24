// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

class Solution {
    func minPathCost(_ grid: [[Int]], _ moveCost: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var dp = grid[0]
        if m > 1 {
            for r in 0..<(m - 1) {
                var next = [Int](repeating: Int.max / 2, count: n)
                for c in 0..<n {
                    let from = grid[r][c]
                    for nc in 0..<n {
                        next[nc] = min(next[nc], dp[c] + moveCost[from][nc] + grid[r + 1][nc])
                    }
                }
                dp = next
            }
        }
        return dp.min()!
    }
}
