// LeetCode 0048 - Rotate Image
// https://leetcode.com/problems/rotate-image/

object Solution {
  def rotate(matrix: Array[Array[Int]]): Unit = {
    val n = matrix.length

    for (i <- 0 until n; j <- i + 1 until n) {
      val tmp = matrix(i)(j)
      matrix(i)(j) = matrix(j)(i)
      matrix(j)(i) = tmp
    }

    for (row <- matrix) {
      var left = 0
      var right = row.length - 1
      while (left < right) {
        val tmp = row(left)
        row(left) = row(right)
        row(right) = tmp
        left += 1
        right -= 1
      }
    }
  }
}
