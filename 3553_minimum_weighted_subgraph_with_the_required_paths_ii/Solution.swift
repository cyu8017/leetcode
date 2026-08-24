// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

class Solution {
    let LOG = 17
    var parent = [[Int]]()
    var depth = [Int]()
    var dist = [Int]()
    var g = [[[Int]]]()

    func dfs(_ u: Int, _ p: Int) {
        parent[0][u] = p
        for e in g[u] {
            let to = e[0], w = e[1]
            if to == p { continue }
            depth[to] = depth[u] + 1
            dist[to] = dist[u] + w
            dfs(to, u)
        }
    }

    func lca(_ u0: Int, _ v0: Int) -> Int {
        var u = u0, v = v0
        if depth[u] < depth[v] { swap(&u, &v) }
        for k in stride(from: LOG - 1, through: 0, by: -1) {
            if parent[k][u] != -1 && depth[parent[k][u]] >= depth[v] { u = parent[k][u] }
        }
        if u == v { return u }
        for k in stride(from: LOG - 1, through: 0, by: -1) {
            if parent[k][u] != -1 && parent[k][u] != parent[k][v] {
                u = parent[k][u]
                v = parent[k][v]
            }
        }
        return parent[0][u]
    }

    func path(_ u: Int, _ v: Int) -> Int {
        let a = lca(u, v)
        return dist[u] + dist[v] - 2 * dist[a]
    }

    func minimumWeight(_ edges: [[Int]], _ queries: [[Int]]) -> [Int] {
        let n = edges.count + 1
        g = Array(repeating: [], count: n)
        for e in edges {
            g[e[0]].append([e[1], e[2]])
            g[e[1]].append([e[0], e[2]])
        }
        parent = Array(repeating: Array(repeating: -1, count: n), count: LOG)
        depth = Array(repeating: 0, count: n)
        dist = Array(repeating: 0, count: n)
        dfs(0, -1)
        for k in 1..<LOG {
            for v in 0..<n {
                if parent[k - 1][v] != -1 { parent[k][v] = parent[k - 1][parent[k - 1][v]] }
            }
        }
        return queries.map { q in (path(q[0], q[1]) + path(q[1], q[2]) + path(q[0], q[2])) / 2 }
    }
}
