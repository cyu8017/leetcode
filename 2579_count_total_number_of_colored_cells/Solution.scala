// LeetCode 2579 - Count Total Number of Colored Cells
// https://leetcode.com/problems/count-total-number-of-colored-cells/

object Solution {
  def coloredCells(n: Int): Long = {
    1 + 2L * n * (n - 1)
  }
}
