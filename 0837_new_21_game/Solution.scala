// LeetCode 0837 - New 21 Game
// https://leetcode.com/problems/new-21-game/

object Solution {
  def new21Game(n: Int, k: Int, maxPts: Int): Double = {
    if (k == 0 || n >= k - 1 + maxPts) return 1.0
    val dp = Array.ofDim[Double](n + 1)
    dp(0) = 1.0
    var window = 1.0
    var ans = 0.0
    var i = 1
    while (i <= n) {
      dp(i) = window / maxPts
      if (i < k) window += dp(i)
      else ans += dp(i)
      if (i - maxPts >= 0 && i - maxPts < k) window -= dp(i - maxPts)
      i += 1
    }
    ans
  }
}
