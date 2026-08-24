// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

class Solution {
    func eventualSafeNodes(_ graph: [[Int]]) -> [Int] {
        let n = graph.count
        var color = Array(repeating: 0, count: n)
        var ans = [Int]()
        for i in 0..<n where dfs(graph, &color, i) { ans.append(i) }
        return ans
    }

    private func dfs(_ graph: [[Int]], _ color: inout [Int], _ node: Int) -> Bool {
        if color[node] != 0 { return color[node] == 2 }
        color[node] = 1
        for nei in graph[node] {
            if !dfs(graph, &color, nei) { return false }
        }
        color[node] = 2
        return true
    }
}
