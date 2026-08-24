// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

class Solution {
    func findRedundantConnection(_ edges: [[Int]]) -> [Int] {
        var parent = Array(0...edges.count)
        func find(_ x: Int) -> Int {
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        for e in edges {
            let a = find(e[0]), b = find(e[1])
            if a == b { return e }
            parent[a] = b
        }
        return []
    }
}
