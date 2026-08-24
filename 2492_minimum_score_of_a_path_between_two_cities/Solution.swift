// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class Solution {
    func minScore(_ n: Int, _ roads: [[Int]]) -> Int {
        var g = [[(Int, Int)]](repeating: [], count: n + 1)
        for r in roads {
            g[r[0]].append((r[1], r[2]))
            g[r[1]].append((r[0], r[2]))
        }
        var vis = [Bool](repeating: false, count: n + 1)
        var ans = 1 << 30
        var q = [1]
        vis[1] = true
        var i = 0
        while i < q.count {
            let u = q[i]; i += 1
            for (v, w) in g[u] {
                ans = min(ans, w)
                if !vis[v] {
                    vis[v] = true
                    q.append(v)
                }
            }
        }
        return ans
    }
}
