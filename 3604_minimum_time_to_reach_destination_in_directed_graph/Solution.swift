// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

class Solution {
    func minTime(_ n: Int, _ edges: [[Int]]) -> Int {
        var g = Array(repeating: [[Int]](), count: n)
        for e in edges { g[e[0]].append([e[1], e[2], e[3]]) }
        let Inf = Int.max / 4
        var dist = Array(repeating: Inf, count: n)
        dist[0] = 0
        var pq = [(0, 0)]
        while !pq.isEmpty {
            pq.sort { $0.0 < $1.0 }
            let cur = pq.removeFirst()
            let t = cur.0, u = cur.1
            if t != dist[u] { continue }
            if u == n - 1 { return t }
            for e in g[u] {
                var nt = t
                if nt > e[2] { continue }
                if nt < e[1] { nt = e[1] }
                nt += 1
                if nt < dist[e[0]] {
                    dist[e[0]] = nt
                    pq.append((nt, e[0]))
                }
            }
        }
        return dist[n - 1] == Inf ? -1 : dist[n - 1]
    }
}
