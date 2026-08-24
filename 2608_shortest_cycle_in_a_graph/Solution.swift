// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

class Solution {
    func findShortestCycle(_ n: Int, _ edges: [[Int]]) -> Int {
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        let INF = 1_000_000_000
        var ans = INF
        for start in 0..<n {
            var dist = [Int](repeating: -1, count: n)
            var parent = [Int](repeating: -1, count: n)
            var q = [start]
            dist[start] = 0
            var qi = 0
            while qi < q.count {
                let u = q[qi]; qi += 1
                for v in g[u] {
                    if dist[v] < 0 {
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                    } else if parent[u] != v {
                        ans = min(ans, dist[u] + dist[v] + 1)
                    }
                }
            }
        }
        return ans == INF ? -1 : ans
    }
}
