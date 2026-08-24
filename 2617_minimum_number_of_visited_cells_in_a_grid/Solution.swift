// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

class Solution {
    func minimumVisitedCells(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var dist = [[Int]](repeating: [Int](repeating: -1, count: n), count: m)
        var nextC = [[Int]](repeating: Array(0...n), count: m)
        var nextR = [[Int]](repeating: Array(0...m), count: n)
        func find(_ next: inout [Int], _ x: Int) -> Int {
            if next[x] != x { next[x] = find(&next, next[x]) }
            return next[x]
        }
        var q = [(0, 0)]
        dist[0][0] = 1
        var qi = 0
        while qi < q.count {
            let r = q[qi].0, c = q[qi].1
            qi += 1
            if r == m - 1 && c == n - 1 { return dist[r][c] }
            var nc = find(&nextC[r], c + 1)
            while nc <= c + grid[r][c] && nc < n {
                if dist[r][nc] == -1 {
                    dist[r][nc] = dist[r][c] + 1
                    q.append((r, nc))
                }
                nextC[r][nc] = find(&nextC[r], nc + 1)
                nc = find(&nextC[r], nc + 1)
            }
            var nr = find(&nextR[c], r + 1)
            while nr <= r + grid[r][c] && nr < m {
                if dist[nr][c] == -1 {
                    dist[nr][c] = dist[r][c] + 1
                    q.append((nr, c))
                }
                nextR[c][nr] = find(&nextR[c], nr + 1)
                nr = find(&nextR[c], nr + 1)
            }
        }
        return -1
    }
}
