// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

class NumMatrix(matrix: Array<IntArray>) {
    private val matrix: Array<IntArray>
    private val tree: Array<IntArray>
    private val rows: Int
    private val cols: Int

    init {
        rows = matrix.size
        cols = if (rows == 0) 0 else matrix[0].size
        this.matrix = Array(rows) { row -> matrix[row].copyOf() }
        tree = Array(rows + 1) { IntArray(cols + 1) }
        for (row in 0 until rows) {
            for (col in 0 until cols) {
                add(row + 1, col + 1, matrix[row][col])
            }
        }
    }

    fun update(row: Int, col: Int, `val`: Int) {
        val delta = `val` - matrix[row][col]
        matrix[row][col] = `val`
        add(row + 1, col + 1, delta)
    }

    fun sumRegion(row1: Int, col1: Int, row2: Int, col2: Int): Int {
        return prefix(row2 + 1, col2 + 1) -
            prefix(row1, col2 + 1) -
            prefix(row2 + 1, col1) +
            prefix(row1, col1)
    }

    private fun add(row: Int, col: Int, delta: Int) {
        var rowIndex = row
        while (rowIndex <= rows) {
            var colIndex = col
            while (colIndex <= cols) {
                tree[rowIndex][colIndex] += delta
                colIndex += colIndex and -colIndex
            }
            rowIndex += rowIndex and -rowIndex
        }
    }

    private fun prefix(row: Int, col: Int): Int {
        var total = 0
        var rowIndex = row
        while (rowIndex > 0) {
            var colIndex = col
            while (colIndex > 0) {
                total += tree[rowIndex][colIndex]
                colIndex -= colIndex and -colIndex
            }
            rowIndex -= rowIndex and -rowIndex
        }
        return total
    }
}
