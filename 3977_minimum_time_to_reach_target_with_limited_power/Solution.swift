// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/


class Solution {
    func minTimeMaxPower(_ n: Int, _ edges: [[Int]], _ power: Int, _ cost: [Int], _ source: Int, _ target: Int) -> [Int] {
        let INF = Int.max / 4
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges { g[e[0]].append((e[1], e[2])) }
        var dist = Array(repeating: Array(repeating: INF, count: power + 1), count: n)
        var pq = [(0, -power, source)]
        dist[source][power] = 0
        while !pq.isEmpty {
            pq.sort {
                if $0.0 != $1.0 { return $0.0 < $1.0 }
                return $0.1 < $1.1
            }
            let cur = pq.removeFirst()
            let d = cur.0
            var p = -cur.1
            let u = cur.2
            if u == target { return [d, p] }
            if d > dist[u][p] || p < cost[u] { continue }
            p -= cost[u]
            for (v, t) in g[u] {
                let nd = d + t
                if nd < dist[v][p] {
                    dist[v][p] = nd
                    pq.append((nd, -p, v))
                }
            }
        }
        return [-1, -1]
    }
}
