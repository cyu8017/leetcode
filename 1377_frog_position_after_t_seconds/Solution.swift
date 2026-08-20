// LeetCode 1377 - Frog Position After T Seconds
// https://leetcode.com/problems/frog-position-after-t-seconds/

class Solution {
    func frogPosition(_ n: Int, _ edges: [[Int]], _ t: Int, _ target: Int) -> Double {
        var g = Array(repeating: [Int](), count: n + 1)
        for e in edges {
            g[e[0]].append(e[1]); g[e[1]].append(e[0])
        }
        func dfs(_ u: Int, _ p: Int, _ time: Int, _ prob: Double) -> Double {
            let kids = g[u].filter { $0 != p }
            if time == t || kids.isEmpty { return u == target ? prob : 0 }
            return kids.map { dfs($0, u, time + 1, prob / Double(kids.count)) }.reduce(0, +)
        }
        return dfs(1, 0, 0, 1.0)
    }
}
