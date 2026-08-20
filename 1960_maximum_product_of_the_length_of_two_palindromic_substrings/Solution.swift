// LeetCode 1960 - Maximum Product of the Length of Two Palindromic Substrings
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

class Solution {
    func maxProduct(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var radius = Array(repeating: 0, count: n)
        var center = 0, right = 0
        for i in 0..<n {
            if i < right {
                radius[i] = min(right - i, radius[2 * center - i])
            }
            while i - radius[i] - 1 >= 0 && i + radius[i] + 1 < n
                && chars[i - radius[i] - 1] == chars[i + radius[i] + 1] {
                radius[i] += 1
            }
            if i + radius[i] > right {
                center = i
                right = i + radius[i]
            }
        }
        var end = Array(repeating: 1, count: n)
        var start = Array(repeating: 1, count: n)
        for i in 0..<n {
            let r = radius[i]
            end[i + r] = max(end[i + r], 2 * r + 1)
            start[i - r] = max(start[i - r], 2 * r + 1)
        }
        for i in stride(from: n - 2, through: 0, by: -1) {
            end[i] = max(end[i], end[i + 1] - 2)
        }
        for i in 1..<n {
            start[i] = max(start[i], start[i - 1] - 2)
        }
        var pre = Array(repeating: 0, count: n)
        pre[0] = end[0]
        for i in 1..<n { pre[i] = max(pre[i - 1], end[i]) }
        var suf = Array(repeating: 0, count: n)
        suf[n - 1] = start[n - 1]
        for i in stride(from: n - 2, through: 0, by: -1) {
            suf[i] = max(suf[i + 1], start[i])
        }
        var ans = 0
        for i in 0..<(n - 1) {
            ans = max(ans, pre[i] * suf[i + 1])
        }
        return ans
    }
}
