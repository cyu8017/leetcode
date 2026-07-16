// LeetCode 0059 - Spiral Matrix II
// https://leetcode.com/problems/spiral-matrix-ii/

object Solution {
  def generateMatrix(n: Int): Array[Array[Int]] = {
    val matrix = Array.fill(n, n)(0)
    var top = 0
    var bottom = n - 1
    var left = 0
    var right = n - 1
    var num = 1

    while (top <= bottom && left <= right) {
      var col = left
      while (col <= right) {
        matrix(top)(col) = num
        num += 1
        col += 1
      }
      top += 1

      var row = top
      while (row <= bottom) {
        matrix(row)(right) = num
        num += 1
        row += 1
      }
      right -= 1

      if (top <= bottom) {
        col = right
        while (col >= left) {
          matrix(bottom)(col) = num
          num += 1
          col -= 1
        }
        bottom -= 1
      }

      if (left <= right) {
        row = bottom
        while (row >= top) {
          matrix(row)(left) = num
          num += 1
          row -= 1
        }
        left += 1
      }
    }

    matrix
  }
}
