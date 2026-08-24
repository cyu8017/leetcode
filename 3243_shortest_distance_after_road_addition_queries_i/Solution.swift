// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

class Solution {
    func shortestDistanceAfterQueries(_ n: Int, _ queries: [[Int]]) -> [Int] {
        var g = Array(repeating: [Int](), count: n)
        for i in 0..<(n - 1) { g[i].append(i + 1) }
        return queries.map { q in
            g[q[0]].append(q[1])
            return bfs(g, n)
        }
    }

    private func bfs(_ g: [[Int]], _ n: Int) -> Int {
        var q = [0]
        var vis = Array(repeating: false, count: n)
        vis[0] = true
        var d = 0
        while !q.isEmpty {
            var nq: [Int] = []
            for u in q {
                if u == n - 1 { return d }
                for v in g[u] where !vis[v] {
                    vis[v] = true
                    nq.append(v)
                }
            }
            q = nq
            d += 1
        }
        return -1
    }
}
