// LeetCode 0867 - Transpose Matrix
// https://leetcode.com/problems/transpose-matrix/

object Solution {
  def transpose(matrix: Array[Array[Int]]): Array[Array[Int]] = {
    val m = matrix.length
    val n = matrix(0).length
    val ans = Array.ofDim[Int](n, m)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        ans(j)(i) = matrix(i)(j)
        j += 1
      }
      i += 1
    }
    ans
  }
}
