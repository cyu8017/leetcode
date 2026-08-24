// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

class Solution {
    func reachableNodes(_ n: Int, _ edges: [[Int]], _ restricted: [Int]) -> Int {
        let ban = Set(restricted)
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var vis = [Bool](repeating: false, count: n)
        var q = [0]
        vis[0] = true
        var ans = 0, i = 0
        while i < q.count {
            let u = q[i]; i += 1
            ans += 1
            for v in g[u] where !vis[v] && !ban.contains(v) {
                vis[v] = true
                q.append(v)
            }
        }
        return ans
    }
}
