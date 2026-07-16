// LeetCode 0498 - Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse/

object Solution {
  def findDiagonalOrder(mat: Array[Array[Int]]): Array[Int] = {
    if (mat.isEmpty || mat(0).isEmpty) return Array.empty[Int]
    val rows = mat.length
    val cols = mat(0).length
    val result = Array.fill(rows * cols)(0)
    var row = 0
    var col = 0
    var upward = true
    var index = 0

    while (index < rows * cols) {
      result(index) = mat(row)(col)
      index += 1
      if (upward) {
        if (col == cols - 1) {
          row += 1
          upward = false
        } else if (row == 0) {
          col += 1
          upward = false
        } else {
          row -= 1
          col += 1
        }
      } else {
        if (row == rows - 1) {
          col += 1
          upward = true
        } else if (col == 0) {
          row += 1
          upward = true
        } else {
          row += 1
          col -= 1
        }
      }
    }
    result
  }
}
