// LeetCode 0084 - Largest Rectangle in Histogram
// https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution {
    fun largestRectangleArea(heights: IntArray): Int {
        val stack = ArrayDeque<Int>()
        var maxArea = 0
        val extended = heights + 0

        for (i in extended.indices) {
            val height = extended[i]
            while (stack.isNotEmpty() && extended[stack.last()] > height) {
                val h = extended[stack.removeLast()]
                val width = if (stack.isEmpty()) i else i - stack.last() - 1
                maxArea = maxOf(maxArea, h * width)
            }
            stack.addLast(i)
        }

        return maxArea
    }
}
