// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

class Solution {
    func countPyramids(_ grid: [[Int]]) -> Int {
        return count(grid) + count(grid.reversed())
    }

    private func count(_ g: [[Int]]) -> Int {
        let m = g.count, n = g[0].count
        var dp = g
        var ans = 0
        for i in stride(from: m - 2, through: 0, by: -1) {
            for j in 1..<(n - 1) where g[i][j] == 1 {
                dp[i][j] = 1 + min(dp[i + 1][j - 1], min(dp[i + 1][j], dp[i + 1][j + 1]))
                ans += dp[i][j] - 1
            }
        }
        return ans
    }
}
