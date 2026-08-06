// LeetCode 1317 - Convert Integer to the Sum of Two Zero-Free Integers
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution {
    fun getNoZeroIntegers(n: Int): IntArray {
        fun valid(value: Int) = '0' !in value.toString()
        for (first in 1 until n) {
            if (valid(first) && valid(n - first)) return intArrayOf(first, n - first)
        }
        return intArrayOf()
    }
}
