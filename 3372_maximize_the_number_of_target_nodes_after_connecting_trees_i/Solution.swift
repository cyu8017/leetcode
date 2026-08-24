// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

class Solution {
    func maxTargetNodes(_ edges1: [[Int]], _ edges2: [[Int]], _ k: Int) -> [Int] {
        let n = edges1.count + 1, m = edges2.count + 1
        let g1 = buildTree(n, edges1)
        let g2 = buildTree(m, edges2)
        var cnt1 = Array(repeating: 0, count: n)
        for i in 0..<n { cnt1[i] = countWithin(g1, i, k) }
        var best2 = 0
        if k > 0 {
            for i in 0..<m {
                let c = countWithin(g2, i, k - 1)
                if c > best2 { best2 = c }
            }
        }
        return cnt1.map { $0 + best2 }
    }

    private func buildTree(_ n: Int, _ edges: [[Int]]) -> [[Int]] {
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        return g
    }

    private func countWithin(_ g: [[Int]], _ start: Int, _ k: Int) -> Int {
        if k < 0 { return 0 }
        var vis = Array(repeating: false, count: g.count)
        var q = [(start, 0)]
        vis[start] = true
        var cnt = 0, qi = 0
        while qi < q.count {
            let (u, d) = q[qi]; qi += 1
            cnt += 1
            if d == k { continue }
            for v in g[u] where !vis[v] {
                vis[v] = true
                q.append((v, d + 1))
            }
        }
        return cnt
    }
}
