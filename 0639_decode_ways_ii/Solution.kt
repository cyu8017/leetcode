// LeetCode 0639 - Decode Ways II
// https://leetcode.com/problems/decode-ways-ii/


class Solution {
    fun numDecodings(s: String): Int {
        val MOD = 1_000_000_007L
        val n = s.length
        var prev2 = 1L
        var prev1 = ways1(s[0])
        for (i in 1 until n) {
            val cur = (ways1(s[i]) * prev1 + ways2(s[i - 1], s[i]) * prev2) % MOD
            prev2 = prev1
            prev1 = cur
        }
        return prev1.toInt()
    }

    private fun ways1(c: Char): Long = when (c) {
        '*' -> 9L
        '0' -> 0L
        else -> 1L
    }

    private fun ways2(a: Char, b: Char): Long {
        if (a == '*' && b == '*') return 15L
        if (a == '*') return if (b <= '6') 2L else 1L
        if (b == '*') {
            return when (a) {
                '1' -> 9L
                '2' -> 6L
                else -> 0L
            }
        }
        val num = (a - '0') * 10 + (b - '0')
        return if (num in 10..26) 1L else 0L
    }
}
