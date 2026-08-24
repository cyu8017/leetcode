// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

class Solution {
    func minMaxWeight(_ n: Int, _ edges: [[Int]], _ threshold: Int) -> Int {
        var lo = 1, hi = 1_000_001, ans = -1
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(n, edges, mid) {
                ans = mid
                hi = mid
            } else { lo = mid + 1 }
        }
        return ans
    }

    private func ok(_ n: Int, _ edges: [[Int]], _ mid: Int) -> Bool {
        var g = Array(repeating: [Int](), count: n)
        for e in edges where e[2] <= mid { g[e[1]].append(e[0]) }
        var vis = Array(repeating: false, count: n)
        var q = [0]
        vis[0] = true
        var cnt = 1, qi = 0
        while qi < q.count {
            let u = q[qi]; qi += 1
            for v in g[u] where !vis[v] {
                vis[v] = true
                cnt += 1
                q.append(v)
            }
        }
        return cnt == n
    }
}
