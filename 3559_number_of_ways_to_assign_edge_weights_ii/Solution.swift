// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

class Solution {
    let MOD = 1_000_000_007
    let LOG = 17
    var depth = [Int]()
    var parent = [[Int]]()
    var graph = [[Int]]()

    func dfs(_ u: Int, _ p: Int) {
        parent[0][u] = p
        for v in graph[u] where v != p {
            depth[v] = depth[u] + 1
            dfs(v, u)
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

    func modPow(_ exp0: Int) -> Int {
        var exp = exp0, base = 2, res = 1
        while exp > 0 {
            if (exp & 1) != 0 { res = res * base % MOD }
            base = base * base % MOD
            exp >>= 1
        }
        return res
    }

    func assignEdgeWeights(_ edges: [[Int]], _ queries: [[Int]]) -> [Int] {
        let n = edges.count + 1
        depth = Array(repeating: 0, count: n + 1)
        graph = Array(repeating: [], count: n + 1)
        parent = Array(repeating: Array(repeating: -1, count: n + 1), count: LOG)
        for e in edges {
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        }
        dfs(1, -1)
        for k in 1..<LOG {
            for v in 1...n {
                if parent[k - 1][v] != -1 { parent[k][v] = parent[k - 1][parent[k - 1][v]] }
            }
        }
        var ans = Array(repeating: 0, count: queries.count)
        for i in 0..<queries.count {
            let u = queries[i][0], v = queries[i][1]
            if u == v { ans[i] = 0; continue }
            let a = lca(u, v)
            let d = depth[u] + depth[v] - 2 * depth[a]
            ans[i] = modPow(d - 1)
        }
        return ans
    }
}
