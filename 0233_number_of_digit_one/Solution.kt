// LeetCode 0233 - Number of Digit One
// https://leetcode.com/problems/number-of-digit-one/

class Solution {
    fun countDigitOne(n: Int): Int {
        var count = 0L
        var factor = 1L
        var value = n.toLong()
        while (factor <= value) {
            val lower = value % factor
            val current = (value / factor) % 10
            val higher = value / (factor * 10)
            count += when {
                current == 0L -> higher * factor
                current == 1L -> higher * factor + lower + 1
                else -> (higher + 1) * factor
            }
            factor *= 10
        }
        return count.toInt()
    }
}
