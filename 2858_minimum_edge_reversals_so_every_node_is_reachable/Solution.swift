// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

class Solution {
    private var g: [[(Int, Int)]] = []
    private var ans: [Int] = []

    func minEdgeReversals(_ n: Int, _ edges: [[Int]]) -> [Int] {
        g = Array(repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1]
            g[u].append((v, 0))
            g[v].append((u, 1))
        }
        ans = Array(repeating: 0, count: n)
        dfs1(0, -1)
        dfs2(0, -1)
        return ans
    }

    private func dfs1(_ u: Int, _ p: Int) {
        for (v, ww) in g[u] {
            if v == p { continue }
            ans[0] += ww
            dfs1(v, u)
        }
    }

    private func dfs2(_ u: Int, _ p: Int) {
        for (v, ww) in g[u] {
            if v == p { continue }
            ans[v] = ww == 0 ? ans[u] + 1 : ans[u] - 1
            dfs2(v, u)
        }
    }
}
