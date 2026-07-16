// LeetCode 0304 - Range Sum Query 2D - Immutable
// https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(matrix: Array[Array[Int]]) {
  private val rows = matrix.length
  private val cols = if (rows == 0) 0 else matrix(0).length
  private val prefix = Array.ofDim[Int](rows + 1, cols + 1)

  for (row <- 0 until rows; col <- 0 until cols) {
    prefix(row + 1)(col + 1) = matrix(row)(col) +
      prefix(row)(col + 1) +
      prefix(row + 1)(col) -
      prefix(row)(col)
  }

  def sumRegion(row1: Int, col1: Int, row2: Int, col2: Int): Int = {
    val topLeft = prefix(row1)(col1)
    val topRight = prefix(row1)(col2 + 1)
    val bottomLeft = prefix(row2 + 1)(col1)
    val bottomRight = prefix(row2 + 1)(col2 + 1)
    bottomRight - topRight - bottomLeft + topLeft
  }
}
