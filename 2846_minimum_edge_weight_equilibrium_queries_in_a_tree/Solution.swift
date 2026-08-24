// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

class Solution {
    private var g: [[(Int, Int)]] = []
    private var up: [[Int]] = []
    private var depth: [Int] = []
    private var cnt: [[Int]] = []
    private let logN = 15

    func minOperationsQueries(_ n: Int, _ edges: [[Int]], _ queries: [[Int]]) -> [Int] {
        g = Array(repeating: [], count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }
        up = Array(repeating: Array(repeating: 0, count: n), count: logN)
        depth = Array(repeating: 0, count: n)
        cnt = Array(repeating: Array(repeating: 0, count: 27), count: n)
        dfs(0, 0)
        for j in 1..<logN {
            for i in 0..<n {
                up[j][i] = up[j - 1][up[j - 1][i]]
            }
        }
        var ans = Array(repeating: 0, count: queries.count)
        for i in 0..<queries.count {
            let a = queries[i][0], b = queries[i][1]
            let c = lca(a, b)
            let total = depth[a] + depth[b] - 2 * depth[c]
            var best = 0
            for w in 1...26 {
                let f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w]
                best = max(best, f)
            }
            ans[i] = total - best
        }
        return ans
    }

    private func dfs(_ u: Int, _ p: Int) {
        up[0][u] = p
        for (v, w) in g[u] {
            if v == p { continue }
            depth[v] = depth[u] + 1
            cnt[v] = cnt[u]
            cnt[v][w] += 1
            dfs(v, u)
        }
    }

    private func lca(_ a0: Int, _ b0: Int) -> Int {
        var a = a0, b = b0
        if depth[a] < depth[b] { swap(&a, &b) }
        var diff = depth[a] - depth[b]
        for j in 0..<logN {
            if (diff & (1 << j)) != 0 { a = up[j][a] }
        }
        if a == b { return a }
        for j in stride(from: logN - 1, through: 0, by: -1) {
            if up[j][a] != up[j][b] {
                a = up[j][a]
                b = up[j][b]
            }
        }
        return up[0][a]
    }
}
