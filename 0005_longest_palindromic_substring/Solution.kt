// LeetCode 0005 - Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

class Solution {
    fun longestPalindrome(s: String): String {
        var bestStart = 0
        var bestLen = 0

        fun expand(left: Int, right: Int) {
            var l = left
            var r = right
            while (l >= 0 && r < s.length && s[l] == s[r]) {
                l--
                r++
            }
            val len = r - l - 1
            if (len > bestLen) {
                bestLen = len
                bestStart = l + 1
            }
        }

        for (i in s.indices) {
            expand(i, i)
            expand(i, i + 1)
        }

        return s.substring(bestStart, bestStart + bestLen)
    }
}
