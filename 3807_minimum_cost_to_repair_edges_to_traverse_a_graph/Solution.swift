// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

class Solution {
    private var edges = [[Int]]()
    private var n = 0, k = 0

    func minCost(_ n: Int, _ edges: [[Int]], _ k: Int) -> Int {
        self.n = n
        self.k = k
        self.edges = edges.sorted { $0[2] < $1[2] }
        let m = self.edges.count
        if m == 0 { return -1 }
        var l = 0, r = m - 1
        while l < r {
            let mid = (l + r) >> 1
            if check(mid) { r = mid }
            else { l = mid + 1 }
        }
        if check(l) { return self.edges[l][2] }
        return -1
    }

    private func check(_ idx: Int) -> Bool {
        var g = [[Int]](repeating: [], count: n)
        for i in 0...idx {
            g[edges[i][0]].append(edges[i][1])
            g[edges[i][1]].append(edges[i][0])
        }
        var q = [0]
        var vis = [Bool](repeating: false, count: n)
        vis[0] = true
        var dist = 0
        while !q.isEmpty {
            var nq = [Int]()
            for u in q {
                if u == n - 1 { return dist <= k }
                for v in g[u] where !vis[v] {
                    vis[v] = true
                    nq.append(v)
                }
            }
            q = nq
            dist += 1
        }
        return false
    }
}
