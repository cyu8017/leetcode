// LeetCode 1914 - Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

class Solution {
    func rotateGrid(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        var grid = grid
        let m = grid.count, n = grid[0].count
        let layers = min(m, n) / 2
        for layer in 0..<layers {
            var vals: [Int] = []
            for c in layer..<(n - layer) { vals.append(grid[layer][c]) }
            for r in (layer + 1)..<(m - layer) { vals.append(grid[r][n - layer - 1]) }
            if m - 2 * layer > 1 {
                for c in stride(from: n - layer - 2, through: layer, by: -1) {
                    vals.append(grid[m - layer - 1][c])
                }
            }
            if n - 2 * layer > 1 {
                for r in stride(from: m - layer - 2, through: layer + 1, by: -1) {
                    vals.append(grid[r][layer])
                }
            }
            let shift = k % vals.count
            vals = Array(vals[shift...]) + Array(vals[..<shift])
            var idx = 0
            for c in layer..<(n - layer) { grid[layer][c] = vals[idx]; idx += 1 }
            for r in (layer + 1)..<(m - layer) { grid[r][n - layer - 1] = vals[idx]; idx += 1 }
            if m - 2 * layer > 1 {
                for c in stride(from: n - layer - 2, through: layer, by: -1) {
                    grid[m - layer - 1][c] = vals[idx]; idx += 1
                }
            }
            if n - 2 * layer > 1 {
                for r in stride(from: m - layer - 2, through: layer + 1, by: -1) {
                    grid[r][layer] = vals[idx]; idx += 1
                }
            }
        }
        return grid
    }
}
