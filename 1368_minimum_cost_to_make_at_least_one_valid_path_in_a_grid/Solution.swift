// LeetCode 1368 - Minimum Cost to Make at Least One Valid Path in a Grid
// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

class Solution {
    func minCost(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var dist = Array(repeating: Array(repeating: Int.max / 4, count: n), count: m)
        dist[0][0] = 0
        var deque = [(0, 0)]
        let dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while !deque.isEmpty {
            let (r, c) = deque.removeFirst()
            for (k, d) in dirs.enumerated() {
                let x = r + d.0, y = c + d.1
                if x >= 0 && x < m && y >= 0 && y < n {
                    let w = (k + 1) != grid[r][c] ? 1 : 0
                    let nd = dist[r][c] + w
                    if nd < dist[x][y] {
                        dist[x][y] = nd
                        if w == 0 { deque.insert((x, y), at: 0) } else { deque.append((x, y)) }
                    }
                }
            }
        }
        return dist[m - 1][n - 1]
    }
}
