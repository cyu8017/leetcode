// LeetCode 0323 - Number of Connected Components in an Undirected Graph
// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

class Solution {
    func countComponents(_ n: Int, _ edges: [[Int]]) -> Int {
        var parent = Array(0..<n)
        var rank = Array(repeating: 0, count: n)

        func find(_ node: Int) -> Int {
            if parent[node] != node {
                parent[node] = find(parent[node])
            }
            return parent[node]
        }

        var components = n
        for edge in edges {
            var rootLeft = find(edge[0])
            var rootRight = find(edge[1])
            if rootLeft == rootRight {
                continue
            }
            if rank[rootLeft] < rank[rootRight] {
                swap(&rootLeft, &rootRight)
            }
            parent[rootRight] = rootLeft
            if rank[rootLeft] == rank[rootRight] {
                rank[rootLeft] += 1
            }
            components -= 1
        }
        return components
    }
}
