// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

class Solution {
    private var g: [[Int]] = []
    private var coins: [Int] = []
    private var k = 0
    private var memo: [Int: Int] = [:]

    func maximumPoints(_ edges: [[Int]], _ coins: [Int], _ k: Int) -> Int {
        let n = coins.count
        self.coins = coins
        self.k = k
        g = Array(repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        memo = [:]
        return dfs(0, -1, 0)
    }

    private func dfs(_ u: Int, _ p: Int, _ shifts0: Int) -> Int {
        var shifts = min(shifts0, 14)
        let key = (u << 5) | shifts
        if let v = memo[key] { return v }
        let c = coins[u] >> shifts
        var opt1 = c - k
        var opt2 = c / 2
        for v in g[u] where v != p {
            opt1 += dfs(v, u, shifts)
            opt2 += dfs(v, u, shifts + 1)
        }
        let best = max(opt1, opt2)
        memo[key] = best
        return best
    }
}
