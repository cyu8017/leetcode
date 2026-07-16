// LeetCode 0240 - Search a 2D Matrix II
// https://leetcode.com/problems/search-a-2d-matrix-ii/

object Solution {
  def searchMatrix(matrix: Array[Array[Int]], target: Int): Boolean = {
    if (matrix.isEmpty || matrix(0).isEmpty) {
      false
    } else {
      var row = 0
      var col = matrix(0).length - 1
      while (row < matrix.length && col >= 0) {
        val value = matrix(row)(col)
        if (value == target) {
          return true
        }
        if (value > target) {
          col -= 1
        } else {
          row += 1
        }
      }
      false
    }
  }
}
