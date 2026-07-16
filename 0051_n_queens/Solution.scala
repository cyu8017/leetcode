// LeetCode 0051 - N-Queens
// https://leetcode.com/problems/n-queens/

object Solution {
  def solveNQueens(n: Int): List[List[String]] = {
    val result = scala.collection.mutable.ListBuffer[List[String]]()
    val cols = scala.collection.mutable.Set[Int]()
    val diag1 = scala.collection.mutable.Set[Int]()
    val diag2 = scala.collection.mutable.Set[Int]()
    val board = Array.fill(n)("." * n)

    def backtrack(row: Int): Unit = {
      if (row == n) {
        result += board.toList
        return
      }

      var col = 0
      while (col < n) {
        if (!cols.contains(col) && !diag1.contains(row + col) && !diag2.contains(row - col)) {
          cols += col
          diag1 += row + col
          diag2 += row - col

          val rowChars = board(row).toCharArray
          rowChars(col) = 'Q'
          board(row) = rowChars.mkString

          backtrack(row + 1)

          cols -= col
          diag1 -= row + col
          diag2 -= row - col
          board(row) = "." * n
        }
        col += 1
      }
    }

    backtrack(0)
    result.toList
  }
}
