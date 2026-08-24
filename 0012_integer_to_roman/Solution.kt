// LeetCode 0012 - Integer to Roman
// https://leetcode.com/problems/integer-to-roman/

class Solution {
    fun intToRoman(num: Int): String {
        val values = intArrayOf(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        val symbols = arrayOf("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        var value = num
        val result = StringBuilder()

        for (i in values.indices) {
            while (value >= values[i]) {
                result.append(symbols[i])
                value -= values[i]
            }
        }

        return result.toString()
    }
}
