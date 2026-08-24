// LeetCode 0880 - Decoded String at Index
// https://leetcode.com/problems/decoded-string-at-index/

class Solution {
    fun decodeAtIndex(s: String, k: Int): String {
        var size = 0L
        for (i in 0 until s.length) {
            var ch = s[i]
            if (ch.isDigit()) size *= ch - '0'
            else size++
        }
        var kk = k.toLong()
        for (i in s.length - 1 downTo 0) {
            var ch = s[i]
            kk %= size
            if (kk == 0 && ch.isLetter()) return ch.toString()
            if (ch.isDigit()) size /= ch - '0'
            else size--
        }
        return ""
    }
}
