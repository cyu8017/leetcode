// LeetCode 0037 - Sudoku Solver
// https://leetcode.com/problems/sudoku-solver/

object Solution {
  def solveSudoku(board: Array[Array[Char]]): Unit = {
    val rows = Array.fill(9)(scala.collection.mutable.Set.empty[Char])
    val cols = Array.fill(9)(scala.collection.mutable.Set.empty[Char])
    val boxes = Array.fill(9)(scala.collection.mutable.Set.empty[Char])
    val empty = scala.collection.mutable.ListBuffer.empty[(Int, Int)]

    for (r <- 0 until 9; c <- 0 until 9) {
      val value = board(r)(c)
      if (value == '.') {
        empty += ((r, c))
      } else {
        val box = (r / 3) * 3 + c / 3
        rows(r).add(value)
        cols(c).add(value)
        boxes(box).add(value)
      }
    }

    def backtrack(index: Int): Boolean = {
      if (index == empty.length) {
        return true
      }

      val (r, c) = empty(index)
      val box = (r / 3) * 3 + c / 3
      for (digit <- '1' to '9') {
        if (!rows(r).contains(digit) && !cols(c).contains(digit) && !boxes(box).contains(digit)) {
          board(r)(c) = digit
          rows(r).add(digit)
          cols(c).add(digit)
          boxes(box).add(digit)

          if (backtrack(index + 1)) {
            return true
          }

          board(r)(c) = '.'
          rows(r).remove(digit)
          cols(c).remove(digit)
          boxes(box).remove(digit)
        }
      }

      false
    }

    backtrack(0)
  }
}
