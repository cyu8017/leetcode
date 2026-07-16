// LeetCode 0296 - Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/

import scala.collection.mutable

object Solution {
  def minTotalDistance(grid: Array[Array[Int]]): Int = {
    val rows = mutable.ListBuffer.empty[Int]
    val cols = mutable.ListBuffer.empty[Int]
    grid.indices.foreach { rowIndex =>
      grid(rowIndex).indices.foreach { colIndex =>
        if (grid(rowIndex)(colIndex) == 1) {
          rows += rowIndex
          cols += colIndex
        }
      }
    }
    val sortedCols = cols.sorted
    val rowMedian = rows(rows.length / 2)
    val colMedian = sortedCols(sortedCols.length / 2)
    rows.map(row => math.abs(row - rowMedian)).sum + sortedCols.map(col => math.abs(col - colMedian)).sum
  }
}
