// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

class Solution {
    func uniquePathsIII(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count
        let n = grid[0].count
        var empty = 0
        var sr = 0, sc = 0
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] != -1 { empty += 1 }
                if grid[i][j] == 1 { sr = i; sc = j }
            }
        }
        var ans = 0
        func dfs(_ r: Int, _ c: Int, _ remain: Int) {
            if grid[r][c] == 2 {
                if remain == 1 { ans += 1 }
                return
            }
            let temp = grid[r][c]
            grid[r][c] = -1
            for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
                let nr = r + dr, nc = c + dc
                if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != -1 {
                    dfs(nr, nc, remain - 1)
                }
            }
            grid[r][c] = temp
        }
        dfs(sr, sc, empty)
        return ans
    }
}
