// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

class Solution {
    var graph = [[Int]]()
    var cost = [Int]()
    var ans = 0

    func minIncrease(_ n: Int, _ edges: [[Int]], _ cost: [Int]) -> Int {
        graph = Array(repeating: [], count: n)
        for e in edges {
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        }
        self.cost = cost
        ans = 0
        _ = dfs(0, -1)
        return ans
    }

    func dfs(_ u: Int, _ p: Int) -> Int {
        if graph[u].count == 1 && p != -1 { return cost[u] }
        var childVals = [Int]()
        for v in graph[u] where v != p { childVals.append(dfs(v, u)) }
        if childVals.isEmpty { return cost[u] }
        var mx = 0
        for c in childVals { mx = max(mx, c) }
        for c in childVals where c < mx { ans += 1 }
        return mx + cost[u]
    }
}
