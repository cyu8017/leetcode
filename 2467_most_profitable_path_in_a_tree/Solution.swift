// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

class Solution {
    func mostProfitablePath(_ edges: [[Int]], _ bob: Int, _ amount: [Int]) -> Int {
        let n = amount.count
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var bobTime = [Int](repeating: n, count: n)
        func findBob(_ u: Int, _ p: Int, _ t: Int) -> Bool {
            if u == 0 {
                bobTime[u] = t
                return true
            }
            for v in g[u] where v != p {
                if findBob(v, u, t + 1) {
                    bobTime[u] = t
                    return true
                }
            }
            return false
        }
        _ = findBob(bob, -1, 0)
        var ans = Int.min
        func dfs(_ u: Int, _ p: Int, _ t: Int, _ income: Int) {
            var cur = amount[u]
            if t > bobTime[u] { cur = 0 }
            else if t == bobTime[u] { cur /= 2 }
            let income = income + cur
            var isLeaf = true
            for v in g[u] where v != p {
                isLeaf = false
                dfs(v, u, t + 1, income)
            }
            if isLeaf { ans = max(ans, income) }
        }
        dfs(0, -1, 0, 0)
        return ans
    }
}
