// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

class Solution {
    func leadsToDestination(_ n: Int, _ edges: [[Int]], _ source: Int, _ destination: Int) -> Bool {
        var graph = Array(repeating: [Int](), count: n)
        for e in edges {
            graph[e[0]].append(e[1])
        }
        var state = Array(repeating: 0, count: n)

        func dfs(_ node: Int) -> Bool {
            if graph[node].isEmpty {
                return node == destination
            }
            if state[node] == 1 { return false }
            if state[node] == 2 { return true }
            state[node] = 1
            for nxt in graph[node] {
                if !dfs(nxt) { return false }
            }
            state[node] = 2
            return true
        }

        return dfs(source)
    }
}
