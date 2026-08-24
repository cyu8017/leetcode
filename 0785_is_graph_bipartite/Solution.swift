// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

class Solution {
    func isBipartite(_ graph: [[Int]]) -> Bool {
        var color = Array(repeating: -1, count: graph.count)
        for node in 0..<graph.count {
            if color[node] == -1 && !dfs(graph, node, 0, &color) { return false }
        }
        return true
    }

    private func dfs(_ graph: [[Int]], _ node: Int, _ c: Int, _ color: inout [Int]) -> Bool {
        color[node] = c
        for nei in graph[node] {
            if color[nei] == -1 {
                if !dfs(graph, nei, c ^ 1, &color) { return false }
            } else if color[nei] == c {
                return false
            }
        }
        return true
    }
}
