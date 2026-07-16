// LeetCode 0069 - Sqrt(x)
// https://leetcode.com/problems/sqrtx/

class Solution {
    fun mySqrt(x: Int): Int {
        if (x < 2) {
            return x
        }

        var left = 2
        var right = x / 2

        while (left <= right) {
            val mid = left + (right - left) / 2
            val square = mid.toLong() * mid
            when {
                square == x.toLong() -> return mid
                square < x.toLong() -> left = mid + 1
                else -> right = mid - 1
            }
        }

        return right
    }
}
