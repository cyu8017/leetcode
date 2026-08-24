// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

class Solution {
    fun monotoneIncreasingDigits(n: Int): Int {
        val digits = n.toString().toCharArray()
        var mark = digits.size
        for (i in digits.size - 1 downTo 1) {
            if (digits[i] < digits[i - 1]) {
                digits[i - 1] = (digits[i - 1].code - 1).toChar()
                mark = i
            }
        }
        for (i in mark until digits.size) digits[i] = '9'
        return String(digits).toInt()
    }
}
