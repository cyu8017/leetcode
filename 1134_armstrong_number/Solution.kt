// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

class Solution {
    fun isArmstrong(n: Int): Boolean {
        val digits = n.toString()
        val power = digits.length
        var sum = 0
        for (d in digits) {
            var p = 1
            repeat(power) { p *= d - '0' }
            sum += p
        }
        return n == sum
    }
}
