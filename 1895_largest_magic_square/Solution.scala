// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

object Solution {
  def largestMagicSquare(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    val rowPrefix = Array.fill(rows, cols + 1)(0)
    val colPrefix = Array.fill(cols, rows + 1)(0)
    for (i <- 0 until rows; j <- 0 until cols) {
      rowPrefix(i)(j + 1) = rowPrefix(i)(j) + grid(i)(j)
      colPrefix(j)(i + 1) = colPrefix(j)(i) + grid(i)(j)
    }

    def rowSum(row: Int, colStart: Int, colEnd: Int): Int =
      rowPrefix(row)(colEnd + 1) - rowPrefix(row)(colStart)

    def colSum(col: Int, rowStart: Int, rowEnd: Int): Int =
      colPrefix(col)(rowEnd + 1) - colPrefix(col)(rowStart)

    def isMagic(rowStart: Int, colStart: Int, size: Int): Boolean = {
      val target = rowSum(rowStart, colStart, colStart + size - 1)
      for (row <- rowStart until rowStart + size) {
        if (rowSum(row, colStart, colStart + size - 1) != target) return false
      }
      for (col <- colStart until colStart + size) {
        if (colSum(col, rowStart, rowStart + size - 1) != target) return false
      }
      var diag1 = 0
      var diag2 = 0
      for (offset <- 0 until size) {
        diag1 += grid(rowStart + offset)(colStart + offset)
        diag2 += grid(rowStart + offset)(colStart + size - 1 - offset)
      }
      diag1 == target && diag2 == target
    }

    for (size <- math.min(rows, cols) to 1 by -1) {
      for (rowStart <- 0 to rows - size; colStart <- 0 to cols - size) {
        if (isMagic(rowStart, colStart, size)) return size
      }
    }
    1
  }
}
