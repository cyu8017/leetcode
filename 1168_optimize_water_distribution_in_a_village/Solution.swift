// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

class Solution {
    func minCostToSupplyWater(_ n: Int, _ wells: [Int], _ pipes: [[Int]]) -> Int {
        var edges = pipes
        for i in 0..<n { edges.append([0, i + 1, wells[i]]) }
        edges.sort { $0[2] < $1[2] }
        var parent = Array(0...n)
        func find(_ x: Int) -> Int {
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        var cost = 0, used = 0
        for e in edges {
            let a = find(e[0]), b = find(e[1])
            if a == b { continue }
            parent[b] = a
            cost += e[2]
            used += 1
            if used == n { break }
        }
        return cost
    }
}
