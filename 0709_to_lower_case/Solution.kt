// LeetCode 0709 - To Lower Case
// https://leetcode.com/problems/to-lower-case/

class Solution {
    fun toLowerCase(s: String): String {
        val chars = s.toCharArray()
        for (i in chars.indices) {
            if (chars[i] in 'A'..'Z') chars[i] = (chars[i].code + 32).toChar()
        }
        return String(chars)
    }
}
