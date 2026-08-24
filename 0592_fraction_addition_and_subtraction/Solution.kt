// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/


class Solution {
    fun fractionAddition(expression: String): String {
        var num = 0L
        var den = 1L
        var i = 0
        val n = expression.length
        while (i < n) {
            var sign = 1
            if (expression[i] == '+' || expression[i] == '-') {
                if (expression[i] == '-') sign = -1
                i++
            }
            var a = 0L
            while (i < n && expression[i].isDigit()) {
                a = a * 10 + (expression[i] - '0')
                i++
            }
            a *= sign
            i++ // skip '/'
            var b = 0L
            while (i < n && expression[i].isDigit()) {
                b = b * 10 + (expression[i] - '0')
                i++
            }
            num = num * b + a * den
            den = den * b
            val g = gcd(kotlin.math.abs(num), den)
            num /= g
            den /= g
        }
        return "$num/$den"
    }

    private fun gcd(a: Long, b: Long): Long {
        var x = a
        var y = b
        while (y != 0L) {
            val t = x % y
            x = y
            y = t
        }
        return x
    }
}
