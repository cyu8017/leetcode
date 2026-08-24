// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

class Solution {
    var g = [[Int]]()
    var cur = 0
    var ans = [Int]()
    var path = [Int]()

    func dfs(_ i: Int, _ x: Int, _ mi: Int, _ mx: Int) {
        if i == 0 {
            let d = max(mx, x) - min(mi, x)
            if d < cur {
                cur = d
                path[i] = x
                ans = path
            }
            return
        }
        for y in g[x] {
            path[i] = y
            dfs(i - 1, x / y, min(mi, y), max(mx, y))
        }
    }

    func minDifference(_ n: Int, _ k: Int) -> [Int] {
        let MX = 100001
        g = Array(repeating: [], count: MX)
        for i in 1..<MX {
            var j = i
            while j < MX { g[j].append(i); j += i }
        }
        cur = Int.max
        ans = []
        path = Array(repeating: 0, count: k)
        dfs(k - 1, n, Int.max, 0)
        return ans
    }
}
