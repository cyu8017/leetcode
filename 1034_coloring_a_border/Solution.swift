// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

class Solution {
    func colorBorder(_ grid: [[Int]], _ row: Int, _ col: Int, _ color: Int) -> [[Int]] {
        var grid = grid
        let m = grid.count, n = grid[0].count
        let original = grid[row][col]
        var component = Set<[Int]>()
        var stack = [[row, col]]
        component.insert([row, col])
        while let cur = stack.popLast() {
            let r = cur[0], c = cur[1]
            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]] {
                let nr = r + d[0], nc = c + d[1]
                if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == original && !component.contains([nr, nc]) {
                    component.insert([nr, nc])
                    stack.append([nr, nc])
                }
            }
        }
        var border = [[Int]]()
        for cell in component {
            let r = cell[0], c = cell[1]
            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]] {
                let nr = r + d[0], nc = c + d[1]
                if !(nr >= 0 && nr < m && nc >= 0 && nc < n) || !component.contains([nr, nc]) {
                    border.append([r, c])
                    break
                }
            }
        }
        for cell in border {
            grid[cell[0]][cell[1]] = color
        }
        return grid
    }
}
