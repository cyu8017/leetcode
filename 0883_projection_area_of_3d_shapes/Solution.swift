// LeetCode 0883 - Projection Area of 3D Shapes
// https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution {
    func projectionArea(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var top = 0, front = 0, side = 0
        for i in 0..<n {
            var rowMax = 0, colMax = 0
            for j in 0..<n {
                if grid[i][j] != 0 { top += 1 }
                rowMax = max(rowMax, grid[i][j])
                colMax = max(colMax, grid[j][i])
            }
            front += rowMax
            side += colMax
        }
        return top + front + side
    }
}
