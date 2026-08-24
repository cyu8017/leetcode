// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

class Solution {
    func constructGridLayout(_ n: Int, _ edges: [[Int]]) -> [[Int]] {
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        let deg = g.map { $0.count }
        var start = 0
        for i in 0..<n {
            if deg[i] == 1 { start = i; break }
            if deg[i] == 2 { start = i }
        }
        var vis = Array(repeating: false, count: n)
        var row = [Int]()
        var cur = start, prev = -1
        while true {
            row.append(cur)
            vis[cur] = true
            var next = -1
            for v in g[cur] {
                if v != prev && !vis[v] && deg[v] <= 3 {
                    next = v
                    if deg[v] < 4 { break }
                }
            }
            if next == -1 { break }
            prev = cur
            cur = next
        }
        var width = row.count
        var height = width != 0 ? n / width : n
        if width == 0 || width * height != n {
            for w in 1...n where n % w == 0 {
                width = w
                height = n / w
                break
            }
        }
        var grid = Array(repeating: Array(repeating: 0, count: width), count: height)
        if row.count == width {
            for c in 0..<width { grid[0][c] = row[c] }
            var used = Array(repeating: false, count: n)
            for x in row { used[x] = true }
            for r in 1..<height {
                for c in 0..<width {
                    let up = grid[r - 1][c]
                    var chosen = -1
                    for v in g[up] {
                        if used[v] { continue }
                        if c == 0 || g[v].contains(grid[r][c - 1]) {
                            chosen = v
                            break
                        }
                    }
                    if chosen == -1 {
                        for v in g[up] where !used[v] { chosen = v; break }
                    }
                    if chosen != -1 {
                        grid[r][c] = chosen
                        used[chosen] = true
                    }
                }
            }
        } else {
            for i in 0..<n { grid[i / width][i % width] = i }
        }
        return grid
    }
}
