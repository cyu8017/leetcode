// LeetCode 1051 - Height Checker
// https://leetcode.com/problems/height-checker/

class Solution {
    fun heightChecker(heights: IntArray): Int {
        val sorted = heights.sortedArray()
        var ans = 0
        for (i in heights.indices) {
            if (heights[i] != sorted[i]) ans++
        }
        return ans
    }
}
