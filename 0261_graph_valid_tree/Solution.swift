// LeetCode 0261 - Graph Valid Tree
// https://leetcode.com/problems/graph-valid-tree/

class Solution {
    func validTree(_ n: Int, _ edges: [[Int]]) -> Bool {
        if edges.count != n - 1 {
            return false
        }
        var parent = Array(0..<n)
        for edge in edges {
            let rootLeft = find(&parent, edge[0])
            let rootRight = find(&parent, edge[1])
            if rootLeft == rootRight {
                return false
            }
            parent[rootLeft] = rootRight
        }
        return true
    }

    private func find(_ parent: inout [Int], _ node: Int) -> Int {
        if parent[node] != node {
            parent[node] = find(&parent, parent[node])
        }
        return parent[node]
    }
}
