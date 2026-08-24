// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

class Solution {
    func assignEdgeWeights(_ edges: [[Int]]) -> Int {
        let mod = 1_000_000_007
        let n = edges.count + 1
        var g = Array(repeating: [Int](), count: n + 1)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        func dfs(_ i: Int, _ fa: Int) -> Int {
            var res = 0
            for j in g[i] where j != fa { res = max(res, dfs(j, i) + 1) }
            return res
        }
        func pow2(_ exp0: Int) -> Int {
            var exp = exp0, a = 2, res = 1
            while exp > 0 {
                if (exp & 1) != 0 { res = res * a % mod }
                a = a * a % mod
                exp >>= 1
            }
            return res
        }
        return pow2(dfs(1, 0) - 1)
    }
}
