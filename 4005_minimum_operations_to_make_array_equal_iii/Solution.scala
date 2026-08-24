// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

import scala.collection.mutable

object Solution {
  private def cost(x: Int, t: Int): Int = {
    if (x == t) 0
    else if (x % t == 0 || t % x == 0) 1
    else 2
  }

  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def minOperations(nums: Array[Int]): Int = {
    val n = nums.length
    if (n <= 1) return 0
    var g = nums(0)
    var mn = nums(0)
    var i = 1
    while (i < n) {
      g = gcd(g, nums(i))
      mn = math.min(mn, nums(i))
      i += 1
    }
    val cands = mutable.HashSet.empty[Int]
    for (x <- nums) cands += x
    var d = 1
    while (1L * d * d <= mn) {
      if (mn % d == 0) {
        cands += d
        cands += mn / d
      }
      d += 1
    }
    cands += g
    var ans = Int.MaxValue
    for (t <- cands) {
      var sum = 0
      var broken = false
      for (x <- nums if !broken) {
        sum += cost(x, t)
        if (sum >= ans) broken = true
      }
      ans = math.min(ans, sum)
    }
    ans
  }
}
