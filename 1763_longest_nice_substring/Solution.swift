// LeetCode 1763 - Longest Nice Substring
// https://leetcode.com/problems/longest-nice-substring/

class Solution {
    func longestNiceSubstring(_ s: String) -> String {
        let chars = Array(s)
        var bestStart = 0
        var bestLen = 0
        for i in 0..<chars.count {
            var lower = 0
            var upper = 0
            for j in i..<chars.count {
                let c = chars[j]
                if c.isLowercase {
                    lower |= 1 << Int(c.asciiValue! - Character("a").asciiValue!)
                } else {
                    upper |= 1 << Int(c.asciiValue! - Character("A").asciiValue!)
                }
                if lower == upper && j - i + 1 > bestLen {
                    bestStart = i
                    bestLen = j - i + 1
                }
            }
        }
        return String(chars[bestStart..<(bestStart + bestLen)])
    }
}
