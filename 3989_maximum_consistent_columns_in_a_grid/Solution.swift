// LeetCode 3989 - Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/


class Solution {
    func maxConsistentColumns(_ grid: [[Int]], _ limit: Int) -> Int {
        let m = grid.count, n = grid[0].count
        var dp = Array(repeating: 0, count: n)
        var ans = 1
        for j in 0..<n {
            dp[j] = 1
            for i in 0..<j {
                if dp[i] + 1 <= dp[j] { continue }
                var ok = true
                for r in 0..<m {
                    if abs(grid[r][j] - grid[r][i]) > limit { ok = false; break }
                }
                if ok { dp[j] = dp[i] + 1 }
            }
            if dp[j] > ans { ans = dp[j] }
        }
        return ans
    }
}
