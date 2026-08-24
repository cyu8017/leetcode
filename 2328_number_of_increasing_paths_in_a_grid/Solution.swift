// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

class Solution {
    func countPaths(_ grid: [[Int]]) -> Int {
        let mod = 1_000_000_007
        let m = grid.count, n = grid[0].count
        var dp = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        func dfs(_ r: Int, _ c: Int) -> Int {
            if dp[r][c] != 0 { return dp[r][c] }
            var res = 1
            for d in dirs {
                let nr = r + d.0, nc = c + d.1
                if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > grid[r][c] {
                    res = (res + dfs(nr, nc)) % mod
                }
            }
            dp[r][c] = res
            return res
        }
        var ans = 0
        for i in 0..<m {
            for j in 0..<n { ans = (ans + dfs(i, j)) % mod }
        }
        return ans
    }
}
