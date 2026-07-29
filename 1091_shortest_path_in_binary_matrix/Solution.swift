// LeetCode 1091 - Shortest Path in Binary Matrix
// https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution {
    func shortestPathBinaryMatrix(_ grid: [[Int]]) -> Int {
        var grid = grid
        let n = grid.count
        if grid[0][0] != 0 || grid[n - 1][n - 1] != 0 {
            return -1
        }
        var queue = [(0, 0, 1)]
        var head = 0
        grid[0][0] = 1
        while head < queue.count {
            let (r, c, dist) = queue[head]
            head += 1
            if r == n - 1 && c == n - 1 {
                return dist
            }
            for dr in -1...1 {
                for dc in -1...1 {
                    if dr == 0 && dc == 0 { continue }
                    let nr = r + dr
                    let nc = c + dc
                    if nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0 {
                        grid[nr][nc] = 1
                        queue.append((nr, nc, dist + 1))
                    }
                }
            }
        }
        return -1
    }
}
