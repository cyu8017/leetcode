// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

class NumMatrix(matrix: Array[Array[Int]]) {
  private val rows = matrix.length
  private val cols = if (rows == 0) 0 else matrix(0).length
  private val matrixCopy = matrix.map(_.clone())
  private val tree = Array.ofDim[Int](rows + 1, cols + 1)

  for (row <- 0 until rows; col <- 0 until cols) {
    add(row + 1, col + 1, matrix(row)(col))
  }

  def update(row: Int, col: Int, `val`: Int): Unit = {
    val delta = `val` - matrixCopy(row)(col)
    matrixCopy(row)(col) = `val`
    add(row + 1, col + 1, delta)
  }

  def sumRegion(row1: Int, col1: Int, row2: Int, col2: Int): Int = {
    prefix(row2 + 1, col2 + 1) -
      prefix(row1, col2 + 1) -
      prefix(row2 + 1, col1) +
      prefix(row1, col1)
  }

  private def add(row: Int, col: Int, delta: Int): Unit = {
    var rowIndex = row
    while (rowIndex <= rows) {
      var colIndex = col
      while (colIndex <= cols) {
        tree(rowIndex)(colIndex) += delta
        colIndex += colIndex & -colIndex
      }
      rowIndex += rowIndex & -rowIndex
    }
  }

  private def prefix(row: Int, col: Int): Int = {
    var total = 0
    var rowIndex = row
    while (rowIndex > 0) {
      var colIndex = col
      while (colIndex > 0) {
        total += tree(rowIndex)(colIndex)
        colIndex -= colIndex & -colIndex
      }
      rowIndex -= rowIndex & -rowIndex
    }
    total
  }
}
