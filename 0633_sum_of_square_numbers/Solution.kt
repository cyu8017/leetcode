// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/


class Solution {
    fun judgeSquareSum(c: Int): Boolean {
        var left = 0L
        var right = kotlin.math.sqrt(c.toDouble()).toLong()
        while (left <= right) {
            val sum = left * left + right * right
            when {
                sum == c.toLong() -> return true
                sum < c -> left++
                else -> right--
            }
        }
        return false
    }
}
