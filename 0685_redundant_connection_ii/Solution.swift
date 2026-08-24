// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

class Solution {
    func findRedundantDirectedConnection(_ edges: [[Int]]) -> [Int] {
        var edges = edges
        let n = edges.count
        var parent = Array(repeating: 0, count: n + 1)
        var cand1: [Int]? = nil
        var cand2: [Int]? = nil
        for i in 0..<n {
            let u = edges[i][0], v = edges[i][1]
            if parent[v] == 0 {
                parent[v] = u
            } else {
                cand1 = [parent[v], v]
                cand2 = [u, v]
                edges[i] = [-1, -1]
                break
            }
        }
        var uf = Array(0...n)
        func find(_ x: Int) -> Int {
            var x = x
            while uf[x] != x {
                uf[x] = uf[uf[x]]
                x = uf[x]
            }
            return x
        }
        for edge in edges {
            if edge[0] < 0 { continue }
            let pu = find(edge[0]), pv = find(edge[1])
            if pu == pv { return cand1 ?? edge }
            uf[pu] = pv
        }
        return cand2!
    }
}
