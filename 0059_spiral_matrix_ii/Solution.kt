// LeetCode 0059 - Spiral Matrix II
// https://leetcode.com/problems/spiral-matrix-ii/

class Solution {
    fun generateMatrix(n: Int): Array<IntArray> {
        val matrix = Array(n) { IntArray(n) }
        var top = 0
        var bottom = n - 1
        var left = 0
        var right = n - 1
        var num = 1

        while (top <= bottom && left <= right) {
            for (col in left..right) {
                matrix[top][col] = num++
            }
            top++

            for (row in top..bottom) {
                matrix[row][right] = num++
            }
            right--

            if (top <= bottom) {
                for (col in right downTo left) {
                    matrix[bottom][col] = num++
                }
                bottom--
            }

            if (left <= right) {
                for (row in bottom downTo top) {
                    matrix[row][left] = num++
                }
                left++
            }
        }

        return matrix
    }
}
