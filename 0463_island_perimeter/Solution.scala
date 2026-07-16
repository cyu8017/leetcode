// LeetCode 0463 - Island Perimeter
// https://leetcode.com/problems/island-perimeter/

object Solution {
  def islandPerimeter(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    var perimeter = 0

    for (row <- 0 until rows; col <- 0 until cols) {
      if (grid(row)(col) != 0) {
        perimeter += 4
        if (row > 0 && grid(row - 1)(col) != 0) {
          perimeter -= 2
        }
        if (col > 0 && grid(row)(col - 1) != 0) {
          perimeter -= 2
        }
      }
    }

    perimeter
  }
}
