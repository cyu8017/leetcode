// LeetCode 0263 - Ugly Number
// https://leetcode.com/problems/ugly-number/

class Solution {
    fun isUgly(n: Int): Boolean {
        var value = n
        if (value <= 0) {
            return false
        }
        for (factor in intArrayOf(2, 3, 5)) {
            while (value % factor == 0) {
                value /= factor
            }
        }
        return value == 1
    }
}
