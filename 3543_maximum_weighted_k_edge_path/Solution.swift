// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

class Solution {
    func maxWeight(_ n: Int, _ edges: [[Int]], _ k: Int, _ t: Int) -> Int {
        var graph = Array(repeating: [[Int]](), count: n)
        for e in edges { graph[e[0]].append([e[1], e[2]]) }
        var dp = Array(repeating: Array(repeating: Set<Int>(), count: k + 1), count: n)
        for u in 0..<n { dp[u][0].insert(0) }
        if k > 0 {
            for i in 0..<k {
                for u in 0..<n {
                    for sum in dp[u][i] {
                        for e in graph[u] {
                            let ns = sum + e[1]
                            if ns < t { dp[e[0]][i + 1].insert(ns) }
                        }
                    }
                }
            }
        }
        var ans = -1
        for u in 0..<n {
            for sum in dp[u][k] { ans = max(ans, sum) }
        }
        return ans
    }
}
