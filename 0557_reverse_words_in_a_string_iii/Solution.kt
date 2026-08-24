// LeetCode 0557 - Reverse Words in a String III
// https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution {
    fun reverseWords(s: String): String {
        val chars = s.toCharArray()
        val n = chars.size
        var start = 0
        for (i in 0..n) {
            if (i == n || chars[i] == ' ') {
                var l = start
                var r = i - 1
                while (l < r) {
                    val tmp = chars[l]
                    chars[l] = chars[r]
                    chars[r] = tmp
                    l++
                    r--
                }
                start = i + 1
            }
        }
        return String(chars)
    }
}
