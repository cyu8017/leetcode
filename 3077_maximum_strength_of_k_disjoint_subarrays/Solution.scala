// LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

object Solution {
  def maximumStrength(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val INF = Long.MinValue / 2
    val f = Array.fill(n + 1, k + 1, 2)(INF)
    f(0)(0)(0) = 0
    var i = 1
    while (i <= n) {
      val x = nums(i - 1).toLong
      var j = 0
      while (j <= k) {
        val sign = if ((j & 1) != 0) 1L else -1L
        val `val` = sign * x * (k - j + 1)
        f(i)(j)(0) = math.max(f(i - 1)(j)(0), f(i - 1)(j)(1))
        f(i)(j)(1) = math.max(f(i)(j)(1), f(i - 1)(j)(1) + `val`)
        if (j > 0) {
          val t = math.max(f(i - 1)(j - 1)(0), f(i - 1)(j - 1)(1)) + `val`
          f(i)(j)(1) = math.max(f(i)(j)(1), t)
        }
        j += 1
      }
      i += 1
    }
    math.max(f(n)(k)(0), f(n)(k)(1))
  }
}
