// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

class Solution {
    func maximalNetworkRank(_ n: Int, _ roads: [[Int]]) -> Int {
        var degree = [Int](repeating: 0, count: n)
        var edges = Set<Int>()
        for road in roads {
            let a = road[0], b = road[1]
            degree[a] += 1
            degree[b] += 1
            edges.insert(min(a, b) * n + max(a, b))
        }
        var ans = 0
        for a in 0..<n {
            for b in (a + 1)..<n {
                let connected = edges.contains(a * n + b) ? 1 : 0
                ans = max(ans, degree[a] + degree[b] - connected)
            }
        }
        return ans
    }
}
