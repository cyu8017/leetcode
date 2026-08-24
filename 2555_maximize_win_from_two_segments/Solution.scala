// LeetCode 2555 - Maximize Win From Two Segments
// https://leetcode.com/problems/maximize-win-from-two-segments/

object Solution {
  def maximizeWin(prizePositions: Array[Int], k: Int): Int = {
    val n = prizePositions.length
    val dp = Array.fill(n + 1)(0)
    var ans = 0
    var left = 0
    var right = 0
    while (right < n) {
      while (prizePositions(right) - prizePositions(left) > k) left += 1
      val cur = right - left + 1
      if (dp(left) + cur > ans) ans = dp(left) + cur
      var best = cur
      if (dp(right) > best) best = dp(right)
      dp(right + 1) = best
      right += 1
    }
    ans
  }
}
