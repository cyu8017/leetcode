// LeetCode 1030 - Matrix Cells in Distance Order
// https://leetcode.com/problems/matrix-cells-in-distance-order/

object Solution {
  def allCellsDistOrder(rows: Int, cols: Int, rCenter: Int, cCenter: Int): Array[Array[Int]] = {
    val cells = (for (r <- 0 until rows; c <- 0 until cols) yield Array(r, c)).toArray
    cells.sortBy(rc => math.abs(rc(0) - rCenter) + math.abs(rc(1) - cCenter))
  }
}
