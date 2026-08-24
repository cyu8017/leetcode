// LeetCode 0782 - Transform to Chessboard
// https://leetcode.com/problems/transform-to-chessboard/

object Solution {
  def movesToChessboard(board: Array[Array[Int]]): Int = {
    val n = board.length
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if ((board(0)(0) ^ board(i)(0) ^ board(0)(j) ^ board(i)(j)) != 0) return -1
        j += 1
      }
      i += 1
    }
    var rowSum = 0
    var colSum = 0
    i = 0
    while (i < n) {
      rowSum += board(0)(i)
      colSum += board(i)(0)
      i += 1
    }
    if (rowSum < n / 2 || rowSum > (n + 1) / 2) return -1
    if (colSum < n / 2 || colSum > (n + 1) / 2) return -1
    var rowSwap = 0
    var colSwap = 0
    i = 0
    while (i < n) {
      if (board(0)(i) != i % 2) rowSwap += 1
      if (board(i)(0) != i % 2) colSwap += 1
      i += 1
    }
    if (n % 2 == 1) {
      if (rowSwap % 2 == 1) rowSwap = n - rowSwap
      if (colSwap % 2 == 1) colSwap = n - colSwap
    } else {
      rowSwap = math.min(rowSwap, n - rowSwap)
      colSwap = math.min(colSwap, n - colSwap)
    }
    (rowSwap + colSwap) / 2
  }
}
