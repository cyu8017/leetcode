// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

class Solution {
    func shortestPath(_ grid: [[Int]], _ k: Int) -> Int {
        let m = grid.count, n = grid[0].count
        if m == 1 && n == 1 { return 0 }
        var seen = [[Int]](repeating: [Int](repeating: -1, count: n), count: m)
        seen[0][0] = k
        var q: [(Int, Int, Int, Int)] = [(0, 0, k, 0)]
        var qi = 0
        let dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while qi < q.count {
            let (r, c, left, dist) = q[qi]; qi += 1
            for (dr, dc) in dirs {
                let nr = r + dr, nc = c + dc
                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                let nleft = left - grid[nr][nc]
                if nleft < 0 { continue }
                if nr == m - 1 && nc == n - 1 { return dist + 1 }
                if seen[nr][nc] < nleft {
                    seen[nr][nc] = nleft
                    q.append((nr, nc, nleft, dist + 1))
                }
            }
        }
        return -1
    }
}
