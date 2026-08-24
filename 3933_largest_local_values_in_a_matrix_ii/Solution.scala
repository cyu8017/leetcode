// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

import scala.collection.mutable

object Solution {
  def countLocalMaximums(matrix: Array[Array[Int]]): Int = {
    val rows = matrix.length
    val cols = matrix(0).length
    val positions = Array.fill(201)(mutable.ArrayBuffer.empty[(Int, Int)])
    var row = 0
    while (row < rows) {
      var col = 0
      while (col < cols) {
        val value = matrix(row)(col)
        if (value > 0) positions(value) += ((row, col))
        col += 1
      }
      row += 1
    }
    var answer = 0
    var value = 1
    while (value <= 200) {
      if (positions(value).nonEmpty) {
        val prefix = Array.ofDim[Int](rows + 1, cols + 1)
        row = 0
        while (row < rows) {
          var col = 0
          while (col < cols) {
            val add = if (matrix(row)(col) > value) 1 else 0
            prefix(row + 1)(col + 1) = prefix(row)(col + 1) + prefix(row + 1)(col) - prefix(row)(col) + add
            col += 1
          }
          row += 1
        }
        for ((r, c) <- positions(value)) {
          val top = math.max(0, r - value)
          val bottom = math.min(rows - 1, r + value)
          val left = math.max(0, c - value)
          val right = math.min(cols - 1, c + value)
          var greater =
            prefix(bottom + 1)(right + 1) - prefix(top)(right + 1) - prefix(bottom + 1)(left) + prefix(top)(left)
          for (dr <- Array(-value, value)) {
            for (dc <- Array(-value, value)) {
              val rr = r + dr
              val cc = c + dc
              if (rr >= 0 && rr < rows && cc >= 0 && cc < cols && matrix(rr)(cc) > value) greater -= 1
            }
          }
          if (greater == 0) answer += 1
        }
      }
      value += 1
    }
    answer
  }
}
