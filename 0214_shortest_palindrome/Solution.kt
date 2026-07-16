// LeetCode 0214 - Shortest Palindrome
// https://leetcode.com/problems/shortest-palindrome/

class Solution {
    fun shortestPalindrome(s: String): String {
        if (s.isEmpty()) return ""
        val reversed = s.reversed()
        val combined = "$s#$reversed"
        val pi = IntArray(combined.length)
        var lps = 0
        for (i in 1 until combined.length) {
            while (lps > 0 && combined[i] != combined[lps]) lps = pi[lps - 1]
            if (combined[i] == combined[lps]) lps++
            pi[i] = lps
        }
        val prefixLen = pi[combined.length - 1]
        return reversed.substring(0, s.length - prefixLen) + s
    }
}
