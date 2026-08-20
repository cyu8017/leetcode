// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

class Solution {
    func minimumCost(_ n: Int, _ connections: [[Int]]) -> Int {
        var parent = Array(0...n)
        func find(_ x: Int) -> Int {
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        var edges = connections.sorted { $0[2] < $1[2] }
        var cost = 0, used = 0
        for e in edges {
            let a = find(e[0]), b = find(e[1])
            if a == b { continue }
            parent[b] = a
            cost += e[2]
            used += 1
            if used == n - 1 { return cost }
        }
        return -1
    }
}
