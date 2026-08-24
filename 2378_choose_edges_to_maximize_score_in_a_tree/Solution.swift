// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

class Solution {
    func maxScore(_ edges: [[Int]]) -> Int {
        let n = edges.count + 1
        var g = [[(Int, Int)]](repeating: [], count: n)
        for i in 1..<n {
            let p = edges[i - 1][0], w = edges[i - 1][1]
            g[p].append((i, w))
            g[i].append((p, w))
        }
        func dfs(_ u: Int, _ p: Int) -> (Int, Int) {
            var base = 0
            var bestGain = 0
            for (to, w) in g[u] where to != p {
                let child = dfs(to, u)
                base += child.0
                bestGain = max(bestGain, child.1 + w - child.0)
            }
            return (base + bestGain, base)
        }
        return dfs(0, -1).0
    }
}
