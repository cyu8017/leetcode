// LeetCode 1392 - Longest Happy Prefix
// https://leetcode.com/problems/longest-happy-prefix/

class Solution {
    func longestPrefix(_ s: String) -> String {
        let chars = Array(s)
        if chars.isEmpty { return "" }
        var pi = Array(repeating: 0, count: chars.count)
        for i in 1..<chars.count {
            var j = pi[i - 1]
            while j > 0 && chars[i] != chars[j] { j = pi[j - 1] }
            if chars[i] == chars[j] { j += 1 }
            pi[i] = j
        }
        return String(chars.prefix(pi[chars.count - 1]))
    }
}
