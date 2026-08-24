// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

object Solution {
  def maximumSumOfHeights(heights: Array[Int]): Long = {
    val n = heights.length
    var ans = 0L
    for (peak <- 0 until n) {
      var sum = heights(peak).toLong
      var mn = heights(peak)
      for (i <- peak - 1 to 0 by -1) {
        if (heights(i) < mn) mn = heights(i)
        sum += mn
      }
      mn = heights(peak)
      for (i <- peak + 1 until n) {
        if (heights(i) < mn) mn = heights(i)
        sum += mn
      }
      if (sum > ans) ans = sum
    }
    ans
  }
}
