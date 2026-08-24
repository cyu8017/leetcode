// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

class Solution {
    func minCostExcludingMax(_ n: Int, _ edges: [[Int]]) -> Int {
        var g = [[[Int]]](repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            g[u].append([v, w])
            g[v].append([u, w])
        }
        let INF = Int(4e18)
        var dist = Array(repeating: [INF, INF], count: n)
        dist[0][0] = 0
        var pq = [(0, 0, 0)]
        while !pq.isEmpty {
            pq.sort { $0.0 < $1.0 }
            let cur = pq.removeFirst()
            let c = cur.0, u = cur.1, used = cur.2
            if c > dist[u][used] { continue }
            if u == n - 1 && used == 1 { return c }
            for e in g[u] {
                let v = e[0], w = e[1]
                var nxt = c + w
                if nxt < dist[v][used] {
                    dist[v][used] = nxt
                    pq.append((nxt, v, used))
                }
                if used == 0 {
                    nxt = c
                    if nxt < dist[v][1] {
                        dist[v][1] = nxt
                        pq.append((nxt, v, 1))
                    }
                }
            }
        }
        return dist[n - 1][1]
    }
}
