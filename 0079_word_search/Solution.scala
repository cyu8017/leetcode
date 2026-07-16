// LeetCode 0079 - Word Search
// https://leetcode.com/problems/word-search/

object Solution {
  def exist(board: Array[Array[Char]], word: String): Boolean = {
    val rows = board.length
    val cols = board(0).length

    def dfs(row: Int, col: Int, index: Int): Boolean = {
      if (index == word.length) {
        return true
      }
      if (
        row < 0
          || col < 0
          || row >= rows
          || col >= cols
          || board(row)(col) != word(index)
      ) {
        return false
      }

      val temp = board(row)(col)
      board(row)(col) = '#'

      val found = dfs(row + 1, col, index + 1)
        || dfs(row - 1, col, index + 1)
        || dfs(row, col + 1, index + 1)
        || dfs(row, col - 1, index + 1)

      board(row)(col) = temp
      found
    }

    for (row <- 0 until rows; col <- 0 until cols) {
      if (dfs(row, col, 0)) {
        return true
      }
    }

    false
  }
}
