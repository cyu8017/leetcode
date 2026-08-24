// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

object Solution {
  def maxSubarraySum(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val pref = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + nums(i)
      i += 1
    }
    val INF = 1L << 62
    val best = Array.fill(k)(INF)
    best(0) = 0
    var ans = -(1L << 62)
    i = 1
    while (i <= n) {
      val r = i % k
      if (best(r) != INF) {
        val cand = pref(i) - best(r)
        if (cand > ans) ans = cand
      }
      if (pref(i) < best(r)) best(r) = pref(i)
      i += 1
    }
    ans
  }
}
