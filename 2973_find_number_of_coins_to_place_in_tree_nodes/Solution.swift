// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

class Solution {
    private var g: [[Int]] = []
    private var cost: [Int] = []
    private var ans: [Int] = []

    func placedCoins(_ edges: [[Int]], _ cost: [Int]) -> [Int] {
        let n = cost.count
        self.cost = cost
        g = Array(repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        ans = Array(repeating: 0, count: n)
        _ = dfs(0, -1)
        return ans
    }

    private func dfs(_ u: Int, _ p: Int) -> [Int] {
        var vals = [cost[u]]
        for v in g[u] where v != p {
            vals.append(contentsOf: dfs(v, u))
        }
        vals.sort()
        if vals.count < 3 {
            ans[u] = 1
        } else {
            let m = vals.count
            let cand1 = vals[m - 1] * vals[m - 2] * vals[m - 3]
            let cand2 = vals[0] * vals[1] * vals[m - 1]
            ans[u] = max(0, max(cand1, cand2))
        }
        if vals.count <= 5 { return vals }
        return [vals[0], vals[1], vals[vals.count - 3], vals[vals.count - 2], vals[vals.count - 1]]
    }
}
