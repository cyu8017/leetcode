// LeetCode 0304 - Range Sum Query 2D - Immutable
// https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(matrix: Array<IntArray>) {
    private val prefix: Array<IntArray>

    init {
        val rows = matrix.size
        val cols = if (rows == 0) 0 else matrix[0].size
        prefix = Array(rows + 1) { IntArray(cols + 1) }
        for (row in 0 until rows) {
            for (col in 0 until cols) {
                prefix[row + 1][col + 1] = matrix[row][col] +
                    prefix[row][col + 1] +
                    prefix[row + 1][col] -
                    prefix[row][col]
            }
        }
    }

    fun sumRegion(row1: Int, col1: Int, row2: Int, col2: Int): Int {
        val topLeft = prefix[row1][col1]
        val topRight = prefix[row1][col2 + 1]
        val bottomLeft = prefix[row2 + 1][col1]
        val bottomRight = prefix[row2 + 1][col2 + 1]
        return bottomRight - topRight - bottomLeft + topLeft
    }
}
