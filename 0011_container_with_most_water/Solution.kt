// LeetCode 0011 - Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

class Solution {
    fun maxArea(height: IntArray): Int {
        var left = 0
        var right = height.size - 1
        var best = 0

        while (left < right) {
            val width = right - left
            best = maxOf(best, minOf(height[left], height[right]) * width)
            if (height[left] < height[right]) {
                left++
            } else {
                right--
            }
        }

        return best
    }
}
