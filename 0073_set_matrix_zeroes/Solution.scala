// LeetCode 0073 - Set Matrix Zeroes
// https://leetcode.com/problems/set-matrix-zeroes/

object Solution {
  def setZeroes(matrix: Array[Array[Int]]): Unit = {
    val rows = matrix.length
    val cols = matrix(0).length
    val firstRowZero = matrix(0).exists(_ == 0)
    val firstColZero = matrix.exists(_(0) == 0)

    for (i <- 1 until rows; j <- 1 until cols) {
      if (matrix(i)(j) == 0) {
        matrix(i)(0) = 0
        matrix(0)(j) = 0
      }
    }

    for (i <- 1 until rows; j <- 1 until cols) {
      if (matrix(i)(0) == 0 || matrix(0)(j) == 0) {
        matrix(i)(j) = 0
      }
    }

    if (firstRowZero) {
      for (j <- 0 until cols) matrix(0)(j) = 0
    }
    if (firstColZero) {
      for (i <- 0 until rows) matrix(i)(0) = 0
    }
  }
}
