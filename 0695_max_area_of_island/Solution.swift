// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

class Solution {
    func maxAreaOfIsland(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        var best = 0
        func dfs(_ r: Int, _ c: Int) -> Int {
            if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 { return 0 }
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        }
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 1 {
                best = max(best, dfs(i, j))
            }
        }
        return best
    }
}
