// LeetCode 0118 - Pascal's Triangle
// https://leetcode.com/problems/pascals-triangle/

object Solution {
  def generate(numRows: Int): List[List[Int]] = {
    var triangle = List[List[Int]]()
    for (row <- 0 until numRows) {
      val values = (0 to row).map { col =>
        if (col == 0 || col == row) 1
        else triangle(row - 1)(col - 1) + triangle(row - 1)(col)
      }.toList
      triangle = triangle :+ values
    }
    triangle
  }
}