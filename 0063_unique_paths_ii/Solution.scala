// LeetCode 0063 - Unique Paths II
// https://leetcode.com/problems/unique-paths-ii/

object Solution {
  def uniquePathsWithObstacles(obstacleGrid: Array[Array[Int]]): Int = {
    if (obstacleGrid(0)(0) == 1) {
      return 0
    }

    val rows = obstacleGrid.length
    val cols = obstacleGrid(0).length
    val row = Array.fill(cols)(0)
    row(0) = 1

    var i = 0
    while (i < rows) {
      if (obstacleGrid(i)(0) == 1) {
        row(0) = 0
      }

      var j = 1
      while (j < cols) {
        if (obstacleGrid(i)(j) == 1) {
          row(j) = 0
        } else {
          row(j) += row(j - 1)
        }
        j += 1
      }
      i += 1
    }

    row(cols - 1)
  }
}
