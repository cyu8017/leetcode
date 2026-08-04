// LeetCode 1370 - Increasing Decreasing String
// https://leetcode.com/problems/increasing-decreasing-string/

class Solution {
    fun sortString(s: String): String {
        val c = IntArray(26)
        for (ch in s) c[ch - 'a']++
        val out = StringBuilder()
        while (out.length < s.length) {
            for (i in 0 until 26) {
                if (c[i] > 0) {
                    out.append(('a'.code + i).toChar())
                    c[i]--
                }
            }
            for (i in 25 downTo 0) {
                if (c[i] > 0) {
                    out.append(('a'.code + i).toChar())
                    c[i]--
                }
            }
        }
        return out.toString()
    }
}
