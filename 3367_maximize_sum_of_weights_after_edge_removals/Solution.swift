// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

class Solution {
    func maximizeSumOfWeights(_ edges: [[Int]], _ k: Int) -> Int {
        let n = edges.count + 1
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }
        func dfs(_ u: Int, _ p: Int) -> (Int, Int) {
            var base = 0
            var gains = [Int]()
            for (to, w) in g[u] where to != p {
                let child = dfs(to, u)
                base += child.1
                let gain = child.0 + w - child.1
                if gain > 0 { gains.append(gain) }
            }
            gains.sort(by: >)
            var with = base, without = base
            for i in 0..<gains.count where i < k - 1 { with += gains[i] }
            for i in 0..<gains.count where i < k { without += gains[i] }
            return (with, without)
        }
        return dfs(0, -1).1
    }
}
