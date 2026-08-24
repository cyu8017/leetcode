// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

class Solution {
    func maximumMinutes(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        let inf = 1_000_000_000
        var fire = [[Int]](repeating: [Int](repeating: inf, count: n), count: m)
        var q: [(Int, Int)] = []
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 1 {
                fire[i][j] = 0
                q.append((i, j))
            }
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var qi = 0
        while qi < q.count {
            let (r, c) = q[qi]; qi += 1
            for d in dirs {
                let nr = r + d.0, nc = c + d.1
                if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || fire[nr][nc] != inf {
                    continue
                }
                fire[nr][nc] = fire[r][c] + 1
                q.append((nr, nc))
            }
        }
        func can(_ wait: Int) -> Bool {
            if wait >= fire[0][0] { return false }
            var vis = [[Bool]](repeating: [Bool](repeating: false, count: n), count: m)
            var qq: [(Int, Int, Int)] = [(0, 0, wait)]
            vis[0][0] = true
            var i = 0
            while i < qq.count {
                let (r, c, t) = qq[i]; i += 1
                for d in dirs {
                    let nr = r + d.0, nc = c + d.1, nt = t + 1
                    if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || vis[nr][nc] {
                        continue
                    }
                    if nr == m - 1 && nc == n - 1 {
                        if nt <= fire[nr][nc] { return true }
                        continue
                    }
                    if nt >= fire[nr][nc] { continue }
                    vis[nr][nc] = true
                    qq.append((nr, nc, nt))
                }
            }
            return false
        }
        var lo = 0, hi = m * n + 10, ans = -1
        while lo <= hi {
            let mid = (lo + hi) / 2
            if can(mid) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        if ans >= m * n { return inf }
        return ans
    }
}
