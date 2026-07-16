// LeetCode 0120 - Triangle
// https://leetcode.com/problems/triangle/

object Solution {
  def minimumTotal(triangle: List[List[Int]]): Int = {
    val dp = Array.fill(triangle.length + 1)(0)
    for (row <- triangle.length - 1 to 0 by -1; col <- 0 to row)
      dp(col) = triangle(row)(col) + Math.min(dp(col), dp(col + 1))
    dp(0)
  }
}