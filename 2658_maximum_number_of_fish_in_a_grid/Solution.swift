// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution {
    func findMaxFish(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        var best = 0
        for i in 0..<m {
            for j in 0..<n where grid[i][j] > 0 {
                best = max(best, dfs(&grid, i, j))
            }
        }
        return best
    }

    private func dfs(_ grid: inout [[Int]], _ r: Int, _ c: Int) -> Int {
        let m = grid.count, n = grid[0].count
        if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 { return 0 }
        let fish = grid[r][c]
        grid[r][c] = 0
        return fish + dfs(&grid, r + 1, c) + dfs(&grid, r - 1, c) + dfs(&grid, r, c + 1) + dfs(&grid, r, c - 1)
    }
}
