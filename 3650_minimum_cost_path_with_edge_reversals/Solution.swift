// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

class Solution {
    func minCost(_ n: Int, _ edges: [[Int]]) -> Int {
        var g = Array(repeating: [[Int]](), count: n)
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            g[u].append([v, w])
            g[v].append([u, w * 2])
        }
        let inf = Int.max / 2
        var dist = Array(repeating: inf, count: n)
        dist[0] = 0
        var pq = [(0, 0)]
        while !pq.isEmpty {
            pq.sort { $0.0 < $1.0 }
            let cur = pq.removeFirst()
            let d = cur.0, u = cur.1
            if d > dist[u] { continue }
            if u == n - 1 { return d }
            for e in g[u] {
                let v = e[0], w = e[1]
                let nd = d + w
                if nd < dist[v] {
                    dist[v] = nd
                    pq.append((nd, v))
                }
            }
        }
        return -1
    }
}
