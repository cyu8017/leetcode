// LeetCode 1959 - Minimum Total Space Wasted With K Resizing Operations
// https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

object Solution {
  def minSpaceWastedKResizing(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val INF = Long.MaxValue / 4
    val waste = Array.ofDim[Long](n, n)
    for (i <- 0 until n) {
      var mx = 0
      var total = 0L
      for (j <- i until n) {
        mx = math.max(mx, nums(j))
        total += nums(j)
        waste(i)(j) = mx.toLong * (j - i + 1) - total
      }
    }
    val segments = k + 1
    val dp = Array.fill(n + 1, segments + 1)(INF)
    dp(0)(0) = 0
    for (i <- 1 to n; s <- 1 to math.min(segments, i); p <- (s - 1) until i) {
      dp(i)(s) = math.min(dp(i)(s), dp(p)(s - 1) + waste(p)(i - 1))
    }
    (1 to segments).map(s => dp(n)(s)).min.toInt
  }
}
