// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

class Solution {
    func areConnected(_ n: Int, _ threshold: Int, _ queries: [[Int]]) -> [Bool] {
        var parent = Array(0...n)
        func find(_ x: Int) -> Int {
            var x = x
            while x != parent[x] {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        if threshold + 1 <= n {
            for d in (threshold + 1)...n {
                var x = 2 * d
                while x <= n {
                    let a = find(d), b = find(x)
                    if a != b { parent[b] = a }
                    x += d
                }
            }
        }
        return queries.map { find($0[0]) == find($0[1]) }
    }
}
