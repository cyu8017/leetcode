// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

object Solution {
  def maxSum(nums: Array[Int], k: Int, m: Int): Long = {
    val n = nums.length
    val pref = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + nums(i)
      i += 1
    }
    val neg = -(1L << 60)
    val dp = Array.fill(k + 1, n + 1)(neg)
    i = 0
    while (i <= n) { dp(0)(i) = 0; i += 1 }
    var t = 1
    while (t <= k) {
      var best = neg
      i = t * m
      while (i <= n) {
        val j = i - m
        best = math.max(best, dp(t - 1)(j) - pref(j))
        dp(t)(i) = best + pref(i)
        i += 1
      }
      i = 1
      while (i <= n) {
        dp(t)(i) = math.max(dp(t)(i), dp(t)(i - 1))
        i += 1
      }
      t += 1
    }
    dp(k)(n)
  }
}
