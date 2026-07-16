// LeetCode 0064 - Minimum Path Sum
// https://leetcode.com/problems/minimum-path-sum/

object Solution {
  def minPathSum(grid: Array[Array[Int]]): Int = {
    val rows = grid.length
    val cols = grid(0).length
    val dp = grid.map(_.clone)

    var i = 0
    while (i < rows) {
      var j = 0
      while (j < cols) {
        if (i == 0 && j == 0) {
          // start cell
        } else if (i == 0) {
          dp(i)(j) += dp(i)(j - 1)
        } else if (j == 0) {
          dp(i)(j) += dp(i - 1)(j)
        } else {
          dp(i)(j) += math.min(dp(i - 1)(j), dp(i)(j - 1))
        }
        j += 1
      }
      i += 1
    }

    dp(rows - 1)(cols - 1)
  }
}
