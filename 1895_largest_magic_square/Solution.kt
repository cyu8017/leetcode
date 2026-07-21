// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

class Solution {
    fun largestMagicSquare(grid: Array<IntArray>): Int {
        val rows = grid.size
        val cols = grid[0].size
        val rowPrefix = Array(rows) { IntArray(cols + 1) }
        val colPrefix = Array(cols) { IntArray(rows + 1) }
        for (i in 0 until rows) {
            for (j in 0 until cols) {
                rowPrefix[i][j + 1] = rowPrefix[i][j] + grid[i][j]
                colPrefix[j][i + 1] = colPrefix[j][i] + grid[i][j]
            }
        }
        fun rowSum(row: Int, colStart: Int, colEnd: Int): Int =
            rowPrefix[row][colEnd + 1] - rowPrefix[row][colStart]
        fun colSum(col: Int, rowStart: Int, rowEnd: Int): Int =
            colPrefix[col][rowEnd + 1] - colPrefix[col][rowStart]
        fun isMagic(rowStart: Int, colStart: Int, size: Int): Boolean {
            val target = rowSum(rowStart, colStart, colStart + size - 1)
            for (row in rowStart until rowStart + size) {
                if (rowSum(row, colStart, colStart + size - 1) != target) return false
            }
            for (col in colStart until colStart + size) {
                if (colSum(col, rowStart, rowStart + size - 1) != target) return false
            }
            var diag1 = 0
            var diag2 = 0
            for (offset in 0 until size) {
                diag1 += grid[rowStart + offset][colStart + offset]
                diag2 += grid[rowStart + offset][colStart + size - 1 - offset]
            }
            return diag1 == target && diag2 == target
        }
        for (size in minOf(rows, cols) downTo 1) {
            for (rowStart in 0..rows - size) {
                for (colStart in 0..cols - size) {
                    if (isMagic(rowStart, colStart, size)) return size
                }
            }
        }
        return 1
    }
}
