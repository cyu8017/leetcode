// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

class Solution {
    func colorGrid(_ n: Int, _ m: Int, _ sources: [[Int]]) -> [[Int]] {
        var ans = Array(repeating: [Int](repeating: 0, count: m), count: n)
        var q = sources
        let dirs = [-1, 0, 1, 0, -1]
        for s in q { ans[s[0]][s[1]] = s[2] }
        while !q.isEmpty {
            var vis = [Int: Int]()
            for curr in q {
                let r = curr[0], c = curr[1], color = curr[2]
                for i in 0..<4 {
                    let x = r + dirs[i], y = c + dirs[i + 1]
                    if x >= 0 && x < n && y >= 0 && y < m && ans[x][y] == 0 {
                        let key = (x << 32) | (y & 0xffffffff)
                        if vis[key] == nil || color > vis[key]! { vis[key] = color }
                    }
                }
            }
            q = []
            for (key, color) in vis {
                let x = key >> 32
                let y = key & 0xffffffff
                ans[x][y] = color
                q.append([x, y, color])
            }
        }
        return ans
    }
}
