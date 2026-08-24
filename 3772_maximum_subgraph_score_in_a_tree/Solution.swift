// LeetCode 3772 - Maximum Subgraph Score In A Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

class Solution {
    func maxSubgraphScore(_ n: Int, _ edges: [[Int]], _ good: [Int]) -> [Int] {
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var parent = [Int](repeating: -2, count: n)
        parent[0] = -1
        var order = [0]
        var i = 0
        while i < order.count {
            let u = order[i]
            for v in g[u] {
                if parent[v] == -2 {
                    parent[v] = u
                    order.append(v)
                }
            }
            i += 1
        }
        var down = [Int](repeating: 0, count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let u = order[i]
            down[u] = 2 * good[u] - 1
            for v in g[u] {
                if parent[v] == u && down[v] > 0 { down[u] += down[v] }
            }
        }
        var ans = down
        for u in order {
            for v in g[u] {
                if parent[v] == u {
                    var outside = ans[u]
                    if down[v] > 0 { outside -= down[v] }
                    ans[v] = down[v]
                    if outside > 0 { ans[v] += outside }
                }
            }
        }
        return ans
    }
}
