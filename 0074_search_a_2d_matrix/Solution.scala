// LeetCode 0074 - Search a 2D Matrix
// https://leetcode.com/problems/search-a-2d-matrix/

object Solution {
  def searchMatrix(matrix: Array[Array[Int]], target: Int): Boolean = {
    var row = 0
    var col = matrix(0).length - 1

    while (row < matrix.length && col >= 0) {
      if (matrix(row)(col) == target) {
        return true
      }
      if (matrix(row)(col) > target) {
        col -= 1
      } else {
        row += 1
      }
    }

    false
  }
}
