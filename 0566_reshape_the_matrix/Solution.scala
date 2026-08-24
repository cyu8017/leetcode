// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/

object Solution {
  def matrixReshape(mat: Array[Array[Int]], r: Int, c: Int): Array[Array[Int]] = {
    val rows = mat.length
    val cols = mat(0).length
    if (rows * cols != r * c) return mat
    val result = Array.ofDim[Int](r, c)
    var index = 0
    var i = 0
    while (i < r) {
      var j = 0
      while (j < c) {
        result(i)(j) = mat(index / cols)(index % cols)
        index += 1
        j += 1
      }
      i += 1
    }
    result
  }
}
