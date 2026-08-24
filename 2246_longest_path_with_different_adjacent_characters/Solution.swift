// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

class Solution {
    func longestPath(_ parent: [Int], _ s: String) -> Int {
        let n = parent.count
        let chars = Array(s)
        var g = [[Int]](repeating: [], count: n)
        for i in 1..<n { g[parent[i]].append(i) }
        var ans = 1
        func dfs(_ u: Int) -> Int {
            var best1 = 0, best2 = 0
            for v in g[u] {
                let lenV = dfs(v)
                if chars[v] == chars[u] { continue }
                if lenV > best1 {
                    best2 = best1
                    best1 = lenV
                } else if lenV > best2 {
                    best2 = lenV
                }
            }
            ans = max(ans, 1 + best1 + best2)
            return 1 + best1
        }
        _ = dfs(0)
        return ans
    }
}
