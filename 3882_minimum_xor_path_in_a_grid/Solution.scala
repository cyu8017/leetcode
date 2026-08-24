// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

object Solution {
  def minXor(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    val dp = Array.fill(cols)(new Array[Boolean](1024))
    var row = 0
    while (row < rows) {
      var left = new Array[Boolean](1024)
      var col = 0
      while (col < cols) {
        val next = new Array[Boolean](1024)
        val value = grid(row)(col)
        if (row == 0 && col == 0) {
          next(value) = true
        } else {
          var xorv = 0
          while (xorv < 1024) {
            if (dp(col)(xorv) || left(xorv)) next(xorv ^ value) = true
            xorv += 1
          }
        }
        dp(col) = next
        left = next
        col += 1
      }
      row += 1
    }
    var xorv = 0
    while (xorv < 1024) {
      if (dp(cols - 1)(xorv)) return xorv
      xorv += 1
    }
    -1
  }
}
