// LeetCode 0008 - String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/

class Solution {
    fun myAtoi(s: String): Int {
        var i = 0
        while (i < s.length && s[i] == ' ') {
            i++
        }
        if (i >= s.length) {
            return 0
        }

        var sign = 1
        if (s[i] == '-') {
            sign = -1
            i++
        } else if (s[i] == '+') {
            i++
        }

        var result = 0
        while (i < s.length && s[i].isDigit()) {
            val digit = s[i] - '0'
            if (result > (Int.MAX_VALUE - digit) / 10) {
                return if (sign == -1) Int.MIN_VALUE else Int.MAX_VALUE
            }
            result = result * 10 + digit
            i++
        }

        return sign * result
    }
}
