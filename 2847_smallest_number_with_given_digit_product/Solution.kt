// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

class Solution {
    fun smallestNumber(n: Long): String {
        if (n == 0) return "0"
        if (n == 1) return "1"
        var digits = StringBuilder()
        for (d in 9 downTo 2) {
            while (n % d == 0) {
                digits.append((char) ('0' + d))
                n /= d
            }
        }
        if (n > 1) return "-1"
        return digits.reverse().toString()
    }
}
