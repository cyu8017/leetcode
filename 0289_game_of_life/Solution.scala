// LeetCode 0289 - Game of Life
// https://leetcode.com/problems/game-of-life/

object Solution {
  def gameOfLife(board: Array[Array[Int]]): Unit = {
    val rows = board.length
    val cols = board(0).length
    for (row <- 0 until rows; col <- 0 until cols) {
      var liveNeighbors = 0
      for (dr <- -1 to 1; dc <- -1 to 1 if dr != 0 || dc != 0) {
        val nextRow = row + dr
        val nextCol = col + dc
        if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols && (board(nextRow)(nextCol) & 1) == 1) {
          liveNeighbors += 1
        }
      }
      if ((board(row)(col) & 1) == 1 && (liveNeighbors == 2 || liveNeighbors == 3)) {
        board(row)(col) |= 2
      } else if ((board(row)(col) & 1) == 0 && liveNeighbors == 3) {
        board(row)(col) |= 2
      }
    }
    for (row <- 0 until rows; col <- 0 until cols) {
      board(row)(col) >>= 1
    }
  }
}
