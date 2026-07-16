// LeetCode 0214 - Shortest Palindrome
// https://leetcode.com/problems/shortest-palindrome/

class Solution {
    func shortestPalindrome(_ s: String) -> String {
        if s.isEmpty {
            return ""
        }
        let reversed = String(s.reversed())
        let combined = s + "#" + reversed
        var pi = Array(repeating: 0, count: combined.count)
        var lps = 0
        let chars = Array(combined)
        for i in 1..<chars.count {
            while lps > 0 && chars[i] != chars[lps] {
                lps = pi[lps - 1]
            }
            if chars[i] == chars[lps] {
                lps += 1
            }
            pi[i] = lps
        }
        let prefixLen = pi[chars.count - 1]
        let prefix = String(reversed.prefix(s.count - prefixLen))
        return prefix + s
    }
}
