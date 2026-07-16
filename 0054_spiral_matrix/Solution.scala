// LeetCode 0054 - Spiral Matrix
// https://leetcode.com/problems/spiral-matrix/

object Solution {
  def spiralOrder(matrix: Array[Array[Int]]): List[Int] = {
    if (matrix.isEmpty) {
      return Nil
    }

    var top = 0
    var bottom = matrix.length - 1
    var left = 0
    var right = matrix(0).length - 1
    val result = scala.collection.mutable.ListBuffer[Int]()

    while (top <= bottom && left <= right) {
      var col = left
      while (col <= right) {
        result += matrix(top)(col)
        col += 1
      }
      top += 1

      var row = top
      while (row <= bottom) {
        result += matrix(row)(right)
        row += 1
      }
      right -= 1

      if (top <= bottom) {
        col = right
        while (col >= left) {
          result += matrix(bottom)(col)
          col -= 1
        }
        bottom -= 1
      }

      if (left <= right) {
        row = bottom
        while (row >= top) {
          result += matrix(row)(left)
          row -= 1
        }
        left += 1
      }
    }

    result.toList
  }
}
