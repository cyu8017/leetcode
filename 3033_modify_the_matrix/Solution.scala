// LeetCode 3033 - Modify the Matrix
// https://leetcode.com/problems/modify-the-matrix/

object Solution {
  def modifiedMatrix(matrix: Array[Array[Int]]): Array[Array[Int]] = {
    val m = matrix.length
    val n = matrix(0).length
    var j = 0
    while (j < n) {
      var mx = -1
      var i = 0
      while (i < m) { mx = math.max(mx, matrix(i)(j)); i += 1 }
      i = 0
      while (i < m) {
        if (matrix(i)(j) == -1) matrix(i)(j) = mx
        i += 1
      }
      j += 1
    }
    matrix
  }
}
