// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

class Solution {
    func getMaximumGold(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        var ans = 0
        func dfs(_ r: Int, _ c: Int) -> Int {
            let gold = grid[r][c]
            grid[r][c] = 0
            var best = 0
            for (dr, dc) in [(1,0),(-1,0),(0,1),(0,-1)] {
                let nr = r + dr, nc = c + dc
                if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != 0 {
                    best = max(best, dfs(nr, nc))
                }
            }
            grid[r][c] = gold
            return gold + best
        }
        for r in 0..<m {
            for c in 0..<n where grid[r][c] != 0 {
                ans = max(ans, dfs(r, c))
            }
        }
        return ans
    }
}
