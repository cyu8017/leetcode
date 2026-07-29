// LeetCode 1067 - Digit Count in Range
// https://leetcode.com/problems/digit-count-in-range/

class Solution {
    fun digitsCount(d: Int, low: Int, high: Int): Int {
        return countUpto(high, d) - countUpto(low - 1, d)
    }

    private fun countUpto(n: Int, d: Int): Int {
        if (n < 0) return 0
        val s = n.toString()
        val length = s.length
        var ans = 0
        for (i in 0 until length) {
            val left = if (i > 0) s.substring(0, i).toInt() else 0
            val right = if (i + 1 < length) s.substring(i + 1).toInt() else 0
            val digit = s[i] - '0'
            val power = pow10(length - i - 1)
            if (d != 0) {
                ans += left * power
                when {
                    digit > d -> ans += power
                    digit == d -> ans += right + 1
                }
            } else {
                if (i == 0) continue
                ans += (left - 1) * power
                if (digit > 0) ans += power else ans += right + 1
            }
        }
        return ans
    }

    private fun pow10(n: Int): Int {
        var p = 1
        repeat(n) { p *= 10 }
        return p
    }
}
