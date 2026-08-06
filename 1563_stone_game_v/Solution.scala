// LeetCode 1563 - Stone Game V
// https://leetcode.com/problems/stone-game-v/

object Solution {
  def stoneGameV(stoneValue: Array[Int]): Int = {
    val n = stoneValue.length
    if (n == 0) return 0
    val pre = Array.fill(n + 1)(0)
    for (i <- 0 until n) pre(i + 1) = pre(i) + stoneValue(i)
    val dp = Array.fill(n, n)(0)
    val left = Array.fill(n, n)(0)
    val right = Array.fill(n, n)(0)
    for (i <- 0 until n) {
      left(i)(i) = stoneValue(i)
      right(i)(i) = stoneValue(i)
    }
    for (length <- 2 to n; i <- 0 to n - length) {
      val j = i + length - 1
      var lo = i
      var hi = j - 1
      while (lo <= hi) {
        val mid = (lo + hi) / 2
        if (2 * (pre(mid + 1) - pre(i)) >= pre(j + 1) - pre(i)) hi = mid - 1
        else lo = mid + 1
      }
      val split = lo
      val leftSum = pre(split + 1) - pre(i)
      val rightSum = pre(j + 1) - pre(split + 1)
      var best = right(split + 1)(j)
      if (leftSum == rightSum) best = math.max(best, left(i)(split))
      else if (split > i) best = math.max(best, left(i)(split - 1))
      dp(i)(j) = best
      val total = pre(j + 1) - pre(i)
      left(i)(j) = math.max(left(i)(j - 1), total + best)
      right(i)(j) = math.max(right(i + 1)(j), total + best)
    }
    dp(0)(n - 1)
  }
}
