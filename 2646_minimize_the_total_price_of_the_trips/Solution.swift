// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

class Solution {
    private var g: [[Int]] = []
    private var price: [Int] = []
    private var cnt: [Int] = []

    func minimumTotalPrice(_ n: Int, _ edges: [[Int]], _ price: [Int], _ trips: [[Int]]) -> Int {
        self.price = price
        g = Array(repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        cnt = Array(repeating: 0, count: n)
        for t in trips { _ = path(t[0], -1, t[1]) }
        let res = dfs(0, -1)
        return min(res.0, res.1)
    }

    private func path(_ u: Int, _ p: Int, _ target: Int) -> Bool {
        if u == target {
            cnt[u] += 1
            return true
        }
        for v in g[u] {
            if v == p { continue }
            if path(v, u, target) {
                cnt[u] += 1
                return true
            }
        }
        return false
    }

    private func dfs(_ u: Int, _ p: Int) -> (Int, Int) {
        var full = price[u] * cnt[u]
        var half = full / 2
        for v in g[u] {
            if v == p { continue }
            let child = dfs(v, u)
            full += min(child.0, child.1)
            half += child.0
        }
        return (full, half)
    }
}
