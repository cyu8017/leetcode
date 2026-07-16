// LeetCode 0120 - Triangle
// https://leetcode.com/problems/triangle/

class Solution {
    fun minimumTotal(triangle: List<List<Int>>): Int {
        val dp = IntArray(triangle.size + 1)
        for (row in triangle.lastIndex downTo 0) {
            for (col in 0..row) {
                dp[col] = triangle[row][col] + minOf(dp[col], dp[col + 1])
            }
        }
        return dp[0]
    }
}