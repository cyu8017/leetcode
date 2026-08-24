// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution {
    func longestCycle(_ edges: [Int]) -> Int {
        let n = edges.count
        var vis = [Bool](repeating: false, count: n)
        var ans = -1
        for i in 0..<n where !vis[i] {
            var dist: [Int: Int] = [:]
            var cur = i, step = 0
            while cur != -1 && !vis[cur] {
                vis[cur] = true
                dist[cur] = step
                cur = edges[cur]
                step += 1
            }
            if cur != -1, let d = dist[cur] {
                ans = max(ans, step - d)
            }
        }
        return ans
    }
}
