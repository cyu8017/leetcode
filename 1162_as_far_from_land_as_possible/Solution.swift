// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution {
    func maxDistance(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var q: [(Int, Int)] = []
        var dist = grid
        for i in 0..<n {
            for j in 0..<n where grid[i][j] == 1 {
                q.append((i, j))
            }
        }
        if q.isEmpty || q.count == n * n { return -1 }
        var ans = -1
        var qi = 0
        let dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while qi < q.count {
            let (r, c) = q[qi]; qi += 1
            for (dr, dc) in dirs {
                let nr = r + dr, nc = c + dc
                if nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == 0 {
                    dist[nr][nc] = dist[r][c] + 1
                    ans = max(ans, dist[nr][nc] - 1)
                    q.append((nr, nc))
                }
            }
        }
        return ans
    }
}
