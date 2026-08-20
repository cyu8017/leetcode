// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

class Solution {
    func treeDiameter(_ edges: [[Int]]) -> Int {
        if edges.isEmpty { return 0 }
        var n = 0
        for e in edges { n = max(n, e[0], e[1]) }
        n += 1
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        func farthest(_ start: Int) -> (Int, Int) {
            var dist = [Int](repeating: -1, count: n)
            dist[start] = 0
            var q = [start], qi = 0
            while qi < q.count {
                let u = q[qi]; qi += 1
                for v in g[u] where dist[v] == -1 {
                    dist[v] = dist[u] + 1
                    q.append(v)
                }
            }
            var best = start
            for i in 0..<n where dist[i] > dist[best] { best = i }
            return (best, dist[best])
        }
        let (u, _) = farthest(0)
        return farthest(u).1
    }
}
