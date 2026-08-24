// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution {
    func minimumObstacles(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var dist = [[Int]](repeating: [Int](repeating: Int.max / 2, count: n), count: m)
        dist[0][0] = 0
        var dq: [(Int, Int)] = [(0, 0)]
        var head = 0
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while head < dq.count {
            let (r, c) = dq[head]; head += 1
            for d in dirs {
                let nr = r + d.0, nc = c + d.1
                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                let nd = dist[r][c] + grid[nr][nc]
                if nd < dist[nr][nc] {
                    dist[nr][nc] = nd
                    if grid[nr][nc] == 0 { dq.insert((nr, nc), at: head) }
                    else { dq.append((nr, nc)) }
                }
            }
        }
        return dist[m - 1][n - 1]
    }
}
