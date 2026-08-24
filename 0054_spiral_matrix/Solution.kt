// LeetCode 0054 - Spiral Matrix
// https://leetcode.com/problems/spiral-matrix/

class Solution {
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        if (matrix.isEmpty()) {
            return emptyList()
        }

        var top = 0
        var bottom = matrix.size - 1
        var left = 0
        var right = matrix[0].size - 1
        val result = mutableListOf<Int>()

        while (top <= bottom && left <= right) {
            for (col in left..right) {
                result.add(matrix[top][col])
            }
            top++

            for (row in top..bottom) {
                result.add(matrix[row][right])
            }
            right--

            if (top <= bottom) {
                for (col in right downTo left) {
                    result.add(matrix[bottom][col])
                }
                bottom--
            }

            if (left <= right) {
                for (row in bottom downTo top) {
                    result.add(matrix[row][left])
                }
                left++
            }
        }

        return result
    }
}
