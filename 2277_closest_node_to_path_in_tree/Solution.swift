// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

class Solution {
    func closestNode(_ n: Int, _ edges: [[Int]], _ query: [[Int]]) -> [Int] {
        let LOG = 17
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var up = [[Int]](repeating: [Int](repeating: 0, count: n), count: LOG)
        var depth = [Int](repeating: 0, count: n)
        func dfs(_ u: Int, _ p: Int) {
            up[0][u] = p
            for v in g[u] where v != p {
                depth[v] = depth[u] + 1
                dfs(v, u)
            }
        }
        dfs(0, 0)
        for k in 1..<LOG {
            for v in 0..<n { up[k][v] = up[k - 1][up[k - 1][v]] }
        }
        func lift(_ v: Int, _ d: Int) -> Int {
            var v = v
            for k in 0..<LOG where ((d >> k) & 1) != 0 { v = up[k][v] }
            return v
        }
        func lca(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            if depth[a] < depth[b] { swap(&a, &b) }
            a = lift(a, depth[a] - depth[b])
            if a == b { return a }
            for k in stride(from: LOG - 1, through: 0, by: -1) {
                if up[k][a] != up[k][b] {
                    a = up[k][a]
                    b = up[k][b]
                }
            }
            return up[0][a]
        }
        func dist(_ a: Int, _ b: Int) -> Int {
            let c = lca(a, b)
            return depth[a] + depth[b] - 2 * depth[c]
        }
        return query.map { q in
            let a = q[0], b = q[1], x = q[2]
            let cands = [lca(a, b), lca(a, x), lca(b, x)]
            var best = cands[0], bestD = dist(cands[0], x)
            for t in 1..<3 {
                let d = dist(cands[t], x)
                if d < bestD {
                    bestD = d
                    best = cands[t]
                }
            }
            return best
        }
    }
}
