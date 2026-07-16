// LeetCode 0537 - Complex Number Multiplication
// https://leetcode.com/problems/complex-number-multiplication/

class Solution {
    fun complexNumberMultiply(num1: String, num2: String): String {
        val (a, b) = parse(num1)
        val (c, d) = parse(num2)
        val real = a * c - b * d
        val imag = a * d + b * c
        return "$real+${imag}i"
    }

    private fun parse(num: String): Pair<Int, Int> {
        val parts = num.split("+")
        return parts[0].toInt() to parts[1].dropLast(1).toInt()
    }
}
