// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

class Solution {
    fun maximumSumOfHeights(heights: List<Int>): Long {
        val n = heights.size
        var ans = 0L
        for (peak in 0 until n) {
            var sum = heights[peak].toLong()
            var mn = heights[peak]
            for (i in peak - 1 downTo 0) {
                if (heights[i] < mn) mn = heights[i]
                sum += mn
            }
            mn = heights[peak]
            for (i in peak + 1 until n) {
                if (heights[i] < mn) mn = heights[i]
                sum += mn
            }
            if (sum > ans) ans = sum
        }
        return ans
    }
}
