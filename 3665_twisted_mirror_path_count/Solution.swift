// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

class Solution {
    var m = 0, n = 0
    var grid = [[Int]]()

    func nextCell(_ i: Int, _ j: Int, _ di0: Int, _ dj0: Int) -> [Int]? {
        var di = di0, dj = dj0
        var ni = i + di, nj = j + dj
        while ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1 {
            if dj == 1 { di = 1; dj = 0 }
            else { di = 0; dj = 1 }
            ni += di
            nj += dj
        }
        if ni < 0 || nj < 0 || ni >= m || nj >= n { return nil }
        return [ni, nj]
    }

    func uniquePaths(_ grid: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        self.grid = grid
        m = grid.count
        n = grid[0].count
        var dp = Array(repeating: Array(repeating: 0, count: n), count: m)
        if grid[0][0] == 1 { return 0 }
        dp[0][0] = 1
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 1 || dp[i][j] == 0 { continue }
                if let a = nextCell(i, j, 0, 1) { dp[a[0]][a[1]] = (dp[a[0]][a[1]] + dp[i][j]) % MOD }
                if let b = nextCell(i, j, 1, 0) { dp[b[0]][b[1]] = (dp[b[0]][b[1]] + dp[i][j]) % MOD }
            }
        }
        return dp[m - 1][n - 1]
    }
}
