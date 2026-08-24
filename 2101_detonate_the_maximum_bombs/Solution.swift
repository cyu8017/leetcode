// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

class Solution {
    func maximumDetonation(_ bombs: [[Int]]) -> Int {
        let n = bombs.count
        var g = [[Int]](repeating: [], count: n)
        for i in 0..<n {
            let x1 = bombs[i][0], y1 = bombs[i][1], r1 = bombs[i][2]
            for j in 0..<n where i != j {
                let dx = bombs[j][0] - x1, dy = bombs[j][1] - y1
                if dx * dx + dy * dy <= r1 * r1 { g[i].append(j) }
            }
        }
        var ans = 0
        for i in 0..<n {
            var vis = [Bool](repeating: false, count: n)
            var q = [i]
            vis[i] = true
            var head = 0, cnt = 0
            while head < q.count {
                let u = q[head]; head += 1; cnt += 1
                for v in g[u] where !vis[v] { vis[v] = true; q.append(v) }
            }
            ans = max(ans, cnt)
        }
        return ans
    }
}
