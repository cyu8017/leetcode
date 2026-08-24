// LeetCode 3503 - Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

class Solution {
    func longestPalindrome(_ s: String, _ t: String) -> Int {
        let s = Array(s)
        var t = Array(t).reversed() as [Character]
        let m = s.count, n = t.count
        func calc(_ str: [Character]) -> [Int] {
            let nn = str.count
            var g = Array(repeating: 0, count: nn)
            func expand(_ l0: Int, _ r0: Int) {
                var l = l0, r = r0
                while l >= 0 && r < nn && str[l] == str[r] {
                    g[l] = max(g[l], r - l + 1)
                    l -= 1; r += 1
                }
            }
            for i in 0..<nn {
                expand(i, i)
                expand(i, i + 1)
            }
            return g
        }
        let g1 = calc(s), g2 = calc(t)
        var ans = 0
        for v in g1 { ans = max(ans, v) }
        for v in g2 { ans = max(ans, v) }
        var f = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        if m >= 1 && n >= 1 {
            for i in 1...m {
                for j in 1...n {
                    if s[i - 1] == t[j - 1] {
                        f[i][j] = f[i - 1][j - 1] + 1
                        let a = i < m ? g1[i] : 0
                        let b = j < n ? g2[j] : 0
                        ans = max(ans, f[i][j] * 2 + a)
                        ans = max(ans, f[i][j] * 2 + b)
                    }
                }
            }
        }
        return ans
    }
}
