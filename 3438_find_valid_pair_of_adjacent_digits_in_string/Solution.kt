// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

class Solution {
    fun findValidPair(s: String): String {
        var freq = IntArray(10)
        for (c in s.toCharArray()) { freq[c - '0']++ }
        var i = 0
        while (i + 1 < s.length) {
            var a = s[i] - '0'
            var b = s[i + 1] - '0'
            if (a != b && freq[a] == a && freq[b] == b) return s.substring(i, i + 2)
            i = i + 1
        }
        return ""
    }
}
