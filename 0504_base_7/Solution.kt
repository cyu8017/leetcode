// LeetCode 0504 - Base 7
// https://leetcode.com/problems/base-7/

class Solution {
    fun convertToBase7(num: Int): String {
        if (num == 0) {
            return "0"
        }
        val negative = num < 0
        var value = kotlin.math.abs(num)
        val digits = StringBuilder()
        while (value > 0) {
            digits.append(value % 7)
            value /= 7
        }
        val result = digits.reverse().toString()
        return if (negative) "-$result" else result
    }
}
