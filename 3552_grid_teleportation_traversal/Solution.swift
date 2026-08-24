// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

class Solution {
    func minMoves(_ matrix: [String]) -> Int {
        let m = matrix.count
        let grid = matrix.map { Array($0) }
        let n = grid[0].count
        var g = [Character: [[Int]]]()
        for i in 0..<m {
            for j in 0..<n {
                let c = grid[i][j]
                if c.isLetter { g[c, default: []].append([i, j]) }
            }
        }
        let dirs = [-1, 0, 1, 0, -1]
        let INF = 1 << 30
        var dist = Array(repeating: Array(repeating: INF, count: n), count: m)
        dist[0][0] = 0
        var q = [[0, 0]]
        var head = 0
        while head < q.count {
            let cur = q[head]; head += 1
            let i = cur[0], j = cur[1], d = dist[i][j]
            if i == m - 1 && j == n - 1 { return d }
            let c = grid[i][j]
            if let pts = g[c] {
                for p in pts {
                    let x = p[0], y = p[1]
                    if d < dist[x][y] {
                        dist[x][y] = d
                        q.insert([x, y], at: head)
                    }
                }
                g[c] = nil
            }
            for idx in 0..<4 {
                let x = i + dirs[idx], y = j + dirs[idx + 1]
                if 0 <= x && x < m && 0 <= y && y < n && grid[x][y] != "#" && d + 1 < dist[x][y] {
                    dist[x][y] = d + 1
                    q.append([x, y])
                }
            }
        }
        return -1
    }
}
