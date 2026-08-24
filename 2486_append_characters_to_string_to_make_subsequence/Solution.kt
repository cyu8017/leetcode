// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution {
    fun appendCharacters(s: String, t: String): Int {
        var j = 0
        var i = 0
        while (i < s.length && j < t.length) {
            if (s[i] == t[j]) j++
            i++
        }
        return t.length - j
    }
}
