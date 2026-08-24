// LeetCode 0766 - Toeplitz Matrix
// https://leetcode.com/problems/toeplitz-matrix/

object Solution {
  def isToeplitzMatrix(matrix: Array[Array[Int]]): Boolean = {
    var r = 1
    while (r < matrix.length) {
      var c = 1
      while (c < matrix(0).length) {
        if (matrix(r)(c) != matrix(r - 1)(c - 1)) return false
        c += 1
      }
      r += 1
    }
    true
  }
}
