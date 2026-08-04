// LeetCode 1392 - Longest Happy Prefix
// https://leetcode.com/problems/longest-happy-prefix/

class Solution {
    fun longestPrefix(s: String): String {
        if (s.isEmpty()) return ""
        val pi = IntArray(s.length)
        for (i in 1 until s.length) {
            var j = pi[i - 1]
            while (j > 0 && s[i] != s[j]) j = pi[j - 1]
            if (s[i] == s[j]) j++
            pi[i] = j
        }
        return s.substring(0, pi.last())
    }
}
