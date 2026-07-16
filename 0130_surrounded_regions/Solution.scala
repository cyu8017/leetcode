// LeetCode 0130 - Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

object Solution {
  def solve(board: Array[Array[Char]]): Unit = {
    if (board.isEmpty || board(0).isEmpty) return
    val rows = board.length
    val cols = board(0).length
    def mark(r: Int, c: Int): Unit = {
      if (r < 0 || r >= rows || c < 0 || c >= cols || board(r)(c) != 'O') return
      board(r)(c) = 'E'
      mark(r + 1, c)
      mark(r - 1, c)
      mark(r, c + 1)
      mark(r, c - 1)
    }
    for (r <- 0 until rows) {
      mark(r, 0)
      mark(r, cols - 1)
    }
    for (c <- 0 until cols) {
      mark(0, c)
      mark(rows - 1, c)
    }
    for (r <- 0 until rows; c <- 0 until cols) {
      if (board(r)(c) == 'O') board(r)(c) = 'X'
      else if (board(r)(c) == 'E') board(r)(c) = 'O'
    }
  }
}