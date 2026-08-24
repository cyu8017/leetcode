// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution {
    func maxTargetNodes(_ edges1: [[Int]], _ edges2: [[Int]]) -> [Int] {
        let n = edges1.count + 1, m = edges2.count + 1
        let g1 = buildTree(n, edges1)
        let g2 = buildTree(m, edges2)
        var color1 = Array(repeating: -1, count: n)
        var color2 = Array(repeating: -1, count: m)
        let c1 = bipartiteCount(g1, &color1)
        let c2 = bipartiteCount(g2, &color2)
        let best2 = max(c2.0, c2.1)
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n { ans[i] = (color1[i] == 0 ? c1.0 : c1.1) + best2 }
        return ans
    }

    private func buildTree(_ n: Int, _ edges: [[Int]]) -> [[Int]] {
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        return g
    }

    private func bipartiteCount(_ g: [[Int]], _ color: inout [Int]) -> (Int, Int) {
        var q = [0]
        color[0] = 0
        var cnt = [1, 0]
        var qi = 0
        while qi < q.count {
            let u = q[qi]; qi += 1
            for v in g[u] where color[v] == -1 {
                color[v] = color[u] ^ 1
                cnt[color[v]] += 1
                q.append(v)
            }
        }
        return (cnt[0], cnt[1])
    }
}
