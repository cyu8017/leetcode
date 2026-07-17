// LeetCode 1730 - Shortest Path to Get Food
// https://leetcode.com/problems/shortest-path-to-get-food/

class Solution {
    func getFood(_ grid: [[Character]]) -> Int {
        let rows = grid.count
        let cols = grid[0].count
        var queue = [(Int, Int, Int)]()
        var seen = [[Bool]](repeating: [Bool](repeating: false, count: cols), count: rows)
        for r in 0..<rows {
            for c in 0..<cols {
                if grid[r][c] == "*" {
                    queue.append((r, c, 0))
                    seen[r][c] = true
                }
            }
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var head = 0
        while head < queue.count {
            let (r, c, d) = queue[head]
            head += 1
            if grid[r][c] == "#" {
                return d
            }
            for (dr, dc) in dirs {
                let nr = r + dr
                let nc = c + dc
                if nr >= 0 && nr < rows && nc >= 0 && nc < cols && !seen[nr][nc] && grid[nr][nc] != "X" {
                    seen[nr][nc] = true
                    queue.append((nr, nc, d + 1))
                }
            }
        }
        return -1
    }
}
