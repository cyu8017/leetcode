// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

object Solution {
  def minOperations(nums: Array[Int], x: Int, k: Int): Long = {
    val n = nums.length
    val minOps = new Array[Long](n - x + 1)
    var i = 0
    while (i + x <= n) {
      val w = java.util.Arrays.copyOfRange(nums, i, i + x)
      java.util.Arrays.sort(w)
      val med = w((x - 1) / 2)
      var ops = 0L
      for (v <- w) ops += math.abs(v - med).toLong
      minOps(i) = ops
      i += 1
    }
    val Inf = 1L << 62
    val dp = Array.fill(n + 1, k + 1)(Inf)
    dp(n)(0) = 0
    i = n - 1
    while (i >= 0) {
      var j = 0
      while (j <= k) {
        dp(i)(j) = dp(i + 1)(j)
        if (j > 0 && i + x <= n && minOps(i) + dp(i + x)(j - 1) < dp(i)(j))
          dp(i)(j) = minOps(i) + dp(i + x)(j - 1)
        j += 1
      }
      i -= 1
    }
    dp(0)(k)
  }
}
