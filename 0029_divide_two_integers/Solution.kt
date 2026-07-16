// LeetCode 0029 - Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

class Solution {
    fun divide(dividend: Int, divisor: Int): Int {
        if (dividend == Int.MIN_VALUE && divisor == -1) {
            return Int.MAX_VALUE
        }

        val negative = (dividend < 0) xor (divisor < 0)
        var a = kotlin.math.abs(dividend.toLong())
        var b = kotlin.math.abs(divisor.toLong())
        var quotient = 0L

        for (i in 31 downTo 0) {
            if ((a shr i) >= b) {
                quotient += 1L shl i
                a -= b shl i
            }
        }

        return if (negative) -quotient.toInt() else quotient.toInt()
    }
}
