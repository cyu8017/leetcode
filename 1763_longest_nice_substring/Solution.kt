// LeetCode 1763 - Longest Nice Substring
// https://leetcode.com/problems/longest-nice-substring/

class Solution {
    fun longestNiceSubstring(s: String): String {
        var bestStart = 0
        var bestLen = 0
        for (i in s.indices) {
            var lower = 0
            var upper = 0
            for (j in i until s.length) {
                val c = s[j]
                if (c.isLowerCase()) {
                    lower = lower or (1 shl (c - 'a'))
                } else {
                    upper = upper or (1 shl (c - 'A'))
                }
                if (lower == upper && j - i + 1 > bestLen) {
                    bestStart = i
                    bestLen = j - i + 1
                }
            }
        }
        return s.substring(bestStart, bestStart + bestLen)
    }
}
