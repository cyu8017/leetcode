// LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

class Solution {
    private var num = 0
    private var x = 0
    private var f: [[Int]] = []

    func findMaximumNumber(_ k: Int, _ x: Int) -> Int {
        self.x = x
        var l = 1, r = 100_000_000_000_000_000
        while l < r {
            let mid = (l + r + 1) >> 1
            num = mid
            var m = 0
            var t = num
            while t > 0 {
                t >>= 1
                m += 1
            }
            f = Array(repeating: Array(repeating: -1, count: 65), count: 65)
            if dfs(m, 0, true) <= k { l = mid }
            else { r = mid - 1 }
        }
        return l
    }

    private func dfs(_ pos: Int, _ cnt: Int, _ limit: Bool) -> Int {
        if pos == 0 { return cnt }
        if !limit && f[pos][cnt] != -1 { return f[pos][cnt] }
        var ans = 0
        let up = limit ? ((num >> (pos - 1)) & 1) : 1
        for i in 0...up {
            var v = cnt
            if i == 1 && pos % x == 0 { v += 1 }
            ans += dfs(pos - 1, v, limit && i == up)
        }
        if !limit { f[pos][cnt] = ans }
        return ans
    }
}
