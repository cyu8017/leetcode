// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

class Solution {
    func minCost(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count, n = grid[0].count
        let inf = Int.max / 4
        var f = Array(repeating: Array(repeating: Array(repeating: inf, count: n), count: m), count: k + 1)
        f[0][0][0] = 0
        for i in 0..<m {
            for j in 0..<n {
                if i > 0 { f[0][i][j] = min(f[0][i][j], f[0][i - 1][j] + grid[i][j]) }
                if j > 0 { f[0][i][j] = min(f[0][i][j], f[0][i][j - 1] + grid[i][j]) }
            }
        }
        var g = [Int: [[Int]]]()
        for i in 0..<m {
            for j in 0..<n { g[grid[i][j], default: []].append([i, j]) }
        }
        let keys = g.keys.sorted(by: >)
        if k >= 1 {
            for t in 1...k {
                var mn = inf
                for key in keys {
                    let pos = g[key]!
                    for p in pos { mn = min(mn, f[t - 1][p[0]][p[1]]) }
                    for p in pos { f[t][p[0]][p[1]] = mn }
                }
                for i in 0..<m {
                    for j in 0..<n {
                        if i > 0 { f[t][i][j] = min(f[t][i][j], f[t][i - 1][j] + grid[i][j]) }
                        if j > 0 { f[t][i][j] = min(f[t][i][j], f[t][i][j - 1] + grid[i][j]) }
                    }
                }
            }
        }
        var ans = inf
        for t in 0...k { ans = min(ans, f[t][m - 1][n - 1]) }
        return ans
    }
}
