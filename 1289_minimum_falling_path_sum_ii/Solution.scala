// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

object Solution {
  def minFallingPathSum(grid: Array[Array[Int]]): Int = {
    var dp = grid(0).clone()
    for (row <- grid.tail) {
      val first = dp.indices.minBy(dp)
      val secondValue = if (dp.length > 1) dp.indices.filter(_ != first).map(dp).min else 0
      dp = row.zipWithIndex.map { case (value, i) =>
        value + (if (i == first) secondValue else dp(first))
      }.toArray
    }
    dp.min
  }
}
