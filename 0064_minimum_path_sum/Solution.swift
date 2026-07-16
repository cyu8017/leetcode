// LeetCode 0064 - Minimum Path Sum
// https://leetcode.com/problems/minimum-path-sum/

class Solution {
    func minPathSum(_ grid: [[Int]]) -> Int {
        var grid = grid
        let rows = grid.count
        let cols = grid[0].count

        for i in 0..<rows {
            for j in 0..<cols {
                if i == 0 && j == 0 {
                    continue
                }
                if i == 0 {
                    grid[i][j] += grid[i][j - 1]
                } else if j == 0 {
                    grid[i][j] += grid[i - 1][j]
                } else {
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                }
            }
        }

        return grid[rows - 1][cols - 1]
    }
}
