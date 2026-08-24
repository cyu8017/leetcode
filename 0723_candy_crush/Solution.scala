// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

object Solution {
  def candyCrush(board: Array[Array[Int]]): Array[Array[Int]] = {
    val m = board.length
    val n = board(0).length
    var stable = false
    while (!stable) {
      stable = true
      var i = 0
      while (i < m) {
        var j = 0
        while (j < n - 2) {
          val value = math.abs(board(i)(j))
          if (value != 0 && value == math.abs(board(i)(j + 1)) && value == math.abs(board(i)(j + 2))) {
            board(i)(j) = -value
            board(i)(j + 1) = -value
            board(i)(j + 2) = -value
            stable = false
          }
          j += 1
        }
        i += 1
      }
      var j = 0
      while (j < n) {
        i = 0
        while (i < m - 2) {
          val value = math.abs(board(i)(j))
          if (value != 0 && value == math.abs(board(i + 1)(j)) && value == math.abs(board(i + 2)(j))) {
            board(i)(j) = -value
            board(i + 1)(j) = -value
            board(i + 2)(j) = -value
            stable = false
          }
          i += 1
        }
        j += 1
      }
      j = 0
      while (j < n) {
        var write = m - 1
        i = m - 1
        while (i >= 0) {
          if (board(i)(j) > 0) {
            board(write)(j) = board(i)(j)
            write -= 1
          }
          i -= 1
        }
        i = write
        while (i >= 0) {
          board(i)(j) = 0
          i -= 1
        }
        j += 1
      }
    }
    board
  }
}
