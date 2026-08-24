// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

class Solution {
    func findSafeWalk(_ grid: [[Int]], _ health: Int) -> Bool {
        let m = grid.count, n = grid[0].count
        var vis = Array(repeating: Array(repeating: -1, count: n), count: m)
        let qh = health - grid[0][0]
        if qh <= 0 { return false }
        var q = [(0, 0, qh)]
        vis[0][0] = qh
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        var qi = 0
        while qi < q.count {
            let (r, c, h) = q[qi]
            qi += 1
            if r == m - 1 && c == n - 1 { return true }
            for (dr, dc) in dirs {
                let nr = r + dr, nc = c + dc
                if nr < 0 || nc < 0 || nr >= m || nc >= n { continue }
                let nh = h - grid[nr][nc]
                if nh <= 0 { continue }
                if nh > vis[nr][nc] {
                    vis[nr][nc] = nh
                    q.append((nr, nc, nh))
                }
            }
        }
        return false
    }
}
