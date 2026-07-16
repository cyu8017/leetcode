// LeetCode 0507 - Perfect Number
// https://leetcode.com/problems/perfect-number/

import kotlin.math.sqrt

class Solution {
    fun checkPerfectNumber(num: Int): Boolean {
        if (num <= 1) {
            return false
        }
        var total = 1
        val limit = sqrt(num.toDouble()).toInt()
        for (divisor in 2..limit) {
            if (num % divisor == 0) {
                total += divisor
                val pair = num / divisor
                if (pair != divisor) {
                    total += pair
                }
            }
        }
        return total == num
    }
}
