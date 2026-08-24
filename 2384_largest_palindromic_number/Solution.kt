// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

class Solution {
    fun largestPalindromic(num: String): String {
        val freq = IntArray(10)
        for (c in num) freq[c - '0']++
        val left = StringBuilder()
        for (d in 9 downTo 0) {
            val pairs = freq[d] / 2
            repeat(pairs) { left.append(('0' + d)) }
            freq[d] %= 2
        }
        var mid = 0.toChar()
        for (d in 9 downTo 0) {
            if (freq[d] > 0) {
                mid = ('0' + d)
                break
            }
        }
        if (left.isEmpty() || left[0] == '0') {
            return if (mid == 0.toChar()) "0" else mid.toString()
        }
        val ans = StringBuilder(left)
        if (mid != 0.toChar()) ans.append(mid)
        ans.append(left.reverse())
        return ans.toString()
    }
}
