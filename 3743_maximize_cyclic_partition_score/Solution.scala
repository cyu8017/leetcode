// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

object Solution {
  def maximumScore(nums: Array[Int], k0: Int): Long = {
    val n = nums.length
    val a = new Array[Int](n * 2)
    System.arraycopy(nums, 0, a, 0, n)
    System.arraycopy(nums, 0, a, n, n)
    var k = k0
    if (k > n) k = n
    var best = 0L
    val NEG = -(1L << 60)
    var start = 0
    while (start < n) {
      val seg = java.util.Arrays.copyOfRange(a, start, start + n)
      val dp = Array.fill(n + 1, k + 1)(NEG)
      dp(0)(0) = 0
      var i = 1
      while (i <= n) {
        var j = 1
        while (j <= k && j <= i) {
          var mx = NEG
          var t = i
          while (t >= j) {
            if (seg(t - 1) > mx) mx = seg(t - 1)
            if (dp(t - 1)(j - 1) > NEG) {
              val cand = dp(t - 1)(j - 1) + mx
              if (cand > dp(i)(j)) dp(i)(j) = cand
            }
            t -= 1
          }
          j += 1
        }
        i += 1
      }
      if (dp(n)(k) > best) best = dp(n)(k)
      start += 1
    }
    best
  }
}
