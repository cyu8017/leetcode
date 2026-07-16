// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

object Solution {
  private val directions = Array(
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
  )

  def updateBoard(board: Array[Array[String]], click: Array[Int]): Array[Array[String]] = {
    val row = click(0)
    val col = click(1)
    if (board(row)(col) == "M") {
      board(row)(col) = "X"
      return board
    }
    reveal(board, row, col)
    board
  }

  private def reveal(board: Array[Array[String]], row: Int, col: Int): Unit = {
    if (row < 0 || row >= board.length || col < 0 || col >= board(0).length || board(row)(col) != "E") {
      return
    }
    val mines = countMines(board, row, col)
    board(row)(col) = if (mines == 0) "B" else mines.toString
    if (mines == 0) {
      for ((dr, dc) <- directions) {
        reveal(board, row + dr, col + dc)
      }
    }
  }

  private def countMines(board: Array[Array[String]], row: Int, col: Int): Int = {
    var total = 0
    for ((dr, dc) <- directions) {
      val nextRow = row + dr
      val nextCol = col + dc
      if (nextRow >= 0 && nextRow < board.length
          && nextCol >= 0 && nextCol < board(0).length
          && board(nextRow)(nextCol) == "M") {
        total += 1
      }
    }
    total
  }
}
