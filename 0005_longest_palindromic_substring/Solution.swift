// LeetCode 0005 - Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

class Solution {
    func longestPalindrome(_ s: String) -> String {
        let chars = Array(s)
        var bestStart = 0
        var bestLen = 0

        func expand(_ left: Int, _ right: Int) {
            var l = left
            var r = right
            while l >= 0 && r < chars.count && chars[l] == chars[r] {
                l -= 1
                r += 1
            }
            let len = r - l - 1
            if len > bestLen {
                bestLen = len
                bestStart = l + 1
            }
        }

        for i in chars.indices {
            expand(i, i)
            expand(i, i + 1)
        }

        let start = chars.index(chars.startIndex, offsetBy: bestStart)
        let end = chars.index(start, offsetBy: bestLen)
        return String(chars[start..<end])
    }
}
