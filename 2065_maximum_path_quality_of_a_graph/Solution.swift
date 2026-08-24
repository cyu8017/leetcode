// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

class Solution {
    func maximalPathQuality(_ values: [Int], _ edges: [[Int]], _ maxTime: Int) -> Int {
        let n = values.count
        var g = [[(Int, Int)]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }
        var vis = [Int](repeating: 0, count: n)
        var ans = 0
        func dfs(_ u: Int, _ time: Int, _ quality: Int) {
            if time > maxTime { return }
            var quality = quality
            if vis[u] == 0 { quality += values[u] }
            vis[u] += 1
            if u == 0 { ans = max(ans, quality) }
            for e in g[u] { dfs(e.0, time + e.1, quality) }
            vis[u] -= 1
        }
        dfs(0, 0, 0)
        return ans
    }
}
