// LeetCode 3504 - Longest Palindrome After Substring Concatenation II
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

class Solution {
    func expand(_ s: [Character], _ g: inout [Int], _ l0: Int, _ r0: Int) {
        var l = l0, r = r0
        while l >= 0 && r < s.count && s[l] == s[r] {
            g[l] = max(g[l], r - l + 1)
            l -= 1
            r += 1
        }
    }

    func calc(_ s: [Character]) -> [Int] {
        let n = s.count
        var g = Array(repeating: 0, count: n)
        for i in 0..<n {
            expand(s, &g, i, i)
            expand(s, &g, i, i + 1)
        }
        return g
    }

    func longestPalindrome(_ s: String, _ t: String) -> Int {
        let sc = Array(s)
        var tc = Array(t)
        tc.reverse()
        let m = sc.count, n = tc.count
        let g1 = calc(sc), g2 = calc(tc)
        var ans = 0
        for v in g1 { ans = max(ans, v) }
        for v in g2 { ans = max(ans, v) }
        var f = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        if m > 0 && n > 0 {
            for i in 1...m {
                for j in 1...n {
                    if sc[i - 1] == tc[j - 1] {
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
