// LeetCode 0892 - Surface Area of 3D Shapes
// https://leetcode.com/problems/surface-area-of-3d-shapes/

class Solution {
    func surfaceArea(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var area = 0
        for i in 0..<n {
            for j in 0..<n where grid[i][j] != 0 {
                area += grid[i][j] * 4 + 2
                if i > 0 { area -= min(grid[i][j], grid[i - 1][j]) * 2 }
                if j > 0 { area -= min(grid[i][j], grid[i][j - 1]) * 2 }
            }
        }
        return area
    }
}
