// LeetCode 0085 - Maximal Rectangle
// https://leetcode.com/problems/maximal-rectangle/

class Solution {
    fun maximalRectangle(matrix: Array<CharArray>): Int {
        if (matrix.isEmpty()) {
            return 0
        }

        val cols = matrix[0].size
        val heights = IntArray(cols)
        var maxArea = 0

        for (row in matrix) {
            for (j in 0 until cols) {
                heights[j] = if (row[j] == '1') heights[j] + 1 else 0
            }
            maxArea = maxOf(maxArea, largestHistogram(heights))
        }

        return maxArea
    }

    private fun largestHistogram(heights: IntArray): Int {
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
