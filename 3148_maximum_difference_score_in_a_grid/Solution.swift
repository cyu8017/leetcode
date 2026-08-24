// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

class Solution {
    func maxScore(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        let INF = 1 << 30
        var f = Array(repeating: Array(repeating: 0, count: n), count: m)
        var ans = -INF
        for i in 0..<m {
            for j in 0..<n {
                let x = grid[i][j]
                var mi = INF
                if i > 0 { mi = min(mi, f[i - 1][j]) }
                if j > 0 { mi = min(mi, f[i][j - 1]) }
                ans = max(ans, x - mi)
                f[i][j] = min(x, mi)
            }
        }
        return ans
    }
}
