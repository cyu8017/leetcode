// LeetCode 0119 - Pascal's Triangle II
// https://leetcode.com/problems/pascals-triangle-ii/

object Solution {
  def getRow(rowIndex: Int): List[Int] = {
    val row = Array.fill(rowIndex + 1)(0)
    row(0) = 1
    for (i <- 1 to rowIndex; j <- i to 1 by -1) row(j) += row(j - 1)
    row.toList
  }
}