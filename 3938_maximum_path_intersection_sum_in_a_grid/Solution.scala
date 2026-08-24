// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

object Solution {
  def maxPathSum(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    var answer = Int.MinValue
    var row = 0
    while (row < rows) {
      val r = row
      answer = math.max(answer, checkLine(cols, col => grid(r)(col)))
      row += 1
    }
    var col = 0
    while (col < cols) {
      val c = col
      answer = math.max(answer, checkLine(rows, r => grid(r)(c)))
      col += 1
    }
    row = 1
    while (row + 1 < rows) {
      col = 1
      while (col + 1 < cols) {
        if (grid(row)(col) > answer) answer = grid(row)(col)
        col += 1
      }
      row += 1
    }
    answer
  }

  private def checkLine(length: Int, value: Int => Int): Int = {
    var answer = Int.MinValue
    var bestEnding = value(0) + value(1)
    if (bestEnding > answer) answer = bestEnding
    var i = 2
    while (i < length) {
      if (value(i - 1) + value(i) > bestEnding + value(i)) bestEnding = value(i - 1) + value(i)
      else bestEnding += value(i)
      if (bestEnding > answer) answer = bestEnding
      i += 1
    }
    answer
  }
}
