// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

class Solution {
    fun alternateDigitSum(n: Int): Int {
        var digits = IntArray(12)
        var len = 0
        var x = n
        while (x > 0) {
            digits[len.also { len = len + 1 }] = x % 10
            x /= 10
        }
        var ans = 0
        var sign = 1
        for (i in len - 1 downTo 0) {
            ans += sign * digits[i]
            sign = -sign
        }
        return ans
    }
}
