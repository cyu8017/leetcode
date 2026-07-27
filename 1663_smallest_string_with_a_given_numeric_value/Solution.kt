// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution {
    fun getSmallestString(n: Int, k: Int): String {
        val a = CharArray(n) { 'a' }
        var rem = k - n
        for (i in n - 1 downTo 0) {
            val d = minOf(25, rem)
            a[i] = ('a'.code + d).toChar()
            rem -= d
        }
        return String(a)
    }
}
