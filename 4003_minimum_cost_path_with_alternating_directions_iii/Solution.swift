// LeetCode 4003 - Minimum Cost Path with Alternating Directions III
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/


class Solution {
    func minCost(_ m: Int, _ n: Int, _ penalty: [[Int]]) -> Int {
        let INF = Int.max / 4
        var dist = Array(repeating: Array(repeating: [INF, INF], count: n), count: m)
        dist[0][0][1] = 1
        var pq = [(1, 0, 0, 1)]
        let dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        while !pq.isEmpty {
            pq.sort { $0.0 < $1.0 }
            let cur = pq.removeFirst()
            let d = cur.0, i = cur.1, j = cur.2, k = cur.3
            if i == m - 1 && j == n - 1 { return d }
            if d > dist[i][j][k] { continue }
            let p = penalty[i][j]
            var nd = d + p
            if nd < dist[i][j][k ^ 1] {
                dist[i][j][k ^ 1] = nd
                pq.append((nd, i, j, k ^ 1))
            }
            for idx in 0..<4 {
                let x = i + dirs[idx][0], y = j + dirs[idx][1]
                if 0 <= x && x < m && 0 <= y && y < n {
                    nd = d + ((x + 1) * (y + 1) + (((idx & 1) ^ k) * p))
                    if nd < dist[x][y][k ^ 1] {
                        dist[x][y][k ^ 1] = nd
                        pq.append((nd, x, y, k ^ 1))
                    }
                }
            }
        }
        return -1
    }
}
