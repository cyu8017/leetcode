// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution {
    func countPairs(_ n: Int, _ edges: [[Int]]) -> Int {
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var vis = [Bool](repeating: false, count: n)
        func dfs(_ u: Int) -> Int {
            vis[u] = true
            var size = 1
            for v in g[u] where !vis[v] { size += dfs(v) }
            return size
        }
        var ans = 0, seen = 0
        for i in 0..<n where !vis[i] {
            let sz = dfs(i)
            ans += sz * seen
            seen += sz
        }
        return ans
    }
}
