// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

object Solution {
  def champagneTower(poured: Int, query_row: Int, query_glass: Int): Double = {
    var row = Array(poured.toDouble)
    var r = 0
    while (r < query_row) {
      val nextRow = Array.ofDim[Double](r + 2)
      var i = 0
      while (i < row.length) {
        val overflow = (row(i) - 1.0) / 2.0
        if (overflow > 0) {
          nextRow(i) += overflow
          nextRow(i + 1) += overflow
        }
        i += 1
      }
      row = nextRow
      r += 1
    }
    math.min(1.0, row(query_glass))
  }
}
