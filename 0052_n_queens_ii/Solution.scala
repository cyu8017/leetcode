// LeetCode 0052 - N-Queens II
// https://leetcode.com/problems/n-queens-ii/

object Solution {
  def totalNQueens(n: Int): Int = {
    var count = 0
    val cols = scala.collection.mutable.Set[Int]()
    val diag1 = scala.collection.mutable.Set[Int]()
    val diag2 = scala.collection.mutable.Set[Int]()

    def backtrack(row: Int): Unit = {
      if (row == n) {
        count += 1
        return
      }

      var col = 0
      while (col < n) {
        if (!cols.contains(col) && !diag1.contains(row + col) && !diag2.contains(row - col)) {
          cols += col
          diag1 += row + col
          diag2 += row - col
          backtrack(row + 1)
          cols -= col
          diag1 -= row + col
          diag2 -= row - col
        }
        col += 1
      }
    }

    backtrack(0)
    count
  }
}
