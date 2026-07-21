// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution {
    fun replaceDigits(s: String): String {
        val chars = s.toCharArray()
        var i = 1
        while (i < chars.size) {
            chars[i] = (chars[i - 1].code + (chars[i] - '0')).toChar()
            i += 2
        }
        return String(chars)
    }
}
