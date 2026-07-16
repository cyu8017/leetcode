// LeetCode 0036 - Valid Sudoku
// https://leetcode.com/problems/valid-sudoku/

object Solution {
  def isValidSudoku(board: Array[Array[Char]]): Boolean = {
    val rows = Array.fill(9)(scala.collection.mutable.Set.empty[Char])
    val cols = Array.fill(9)(scala.collection.mutable.Set.empty[Char])
    val boxes = Array.fill(9)(scala.collection.mutable.Set.empty[Char])

    for (r <- 0 until 9; c <- 0 until 9) {
      val value = board(r)(c)
      if (value != '.') {
        val box = (r / 3) * 3 + c / 3
        if (rows(r).contains(value) || cols(c).contains(value) || boxes(box).contains(value)) {
          return false
        }
        rows(r).add(value)
        cols(c).add(value)
        boxes(box).add(value)
      }
    }

    true
  }
}
