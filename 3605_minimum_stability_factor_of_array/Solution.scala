// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

object Solution {
  def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def ok(nums: Array[Int], maxC: Int, x: Int): Boolean = {
    val n = nums.length
    if (x >= n) return true
    var changes = 0
    var i = 0
    while (i + x < n) {
      var g = nums(i)
      var j = i + 1
      while (j <= i + x) { g = gcd(g, nums(j)); j += 1 }
      if (g > 1) {
        changes += 1
        i += x + 1
      } else i += 1
    }
    changes <= maxC
  }

  def minStable(nums: Array[Int], maxC: Int): Int = {
    val n = nums.length
    var lo = 0
    var hi = n
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(nums, maxC, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }
}
