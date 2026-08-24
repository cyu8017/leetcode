// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

class Solution {
    private var g: [[Int]] = []
    private var values: [Int] = []

    func maximumScoreAfterOperations(_ edges: [[Int]], _ values: [Int]) -> Int {
        let n = values.count
        self.values = values
        g = Array(repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        let total = values.reduce(0, +)
        return total - dfs(0, -1)
    }

    private func dfs(_ u: Int, _ p: Int) -> Int {
        var sumKids = 0
        var isLeaf = true
        for v in g[u] where v != p {
            isLeaf = false
            sumKids += dfs(v, u)
        }
        if isLeaf { return values[u] }
        return min(values[u], sumKids)
    }
}
