// LeetCode 1761 - Minimum Degree of a Connected Trio in a Graph
// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

class Solution {
    func minTrioDegree(_ n: Int, _ edges: [[Int]]) -> Int {
        var adj = Array(repeating: Array(repeating: false, count: n), count: n)
        var degree = Array(repeating: 0, count: n)
        for e in edges {
            let u = e[0] - 1
            let v = e[1] - 1
            adj[u][v] = true
            adj[v][u] = true
            degree[u] += 1
            degree[v] += 1
        }
        var best = Int.max
        for e in edges {
            let u = e[0] - 1
            let v = e[1] - 1
            for k in 0..<n {
                if adj[u][k] && adj[v][k] {
                    best = min(best, degree[u] + degree[v] + degree[k] - 6)
                }
            }
        }
        return best == Int.max ? -1 : best
    }
}
