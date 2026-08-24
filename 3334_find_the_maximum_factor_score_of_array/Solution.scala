// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

object Solution {
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
  private def lcm(a: Int, b: Int): Int = a / gcd(a, b) * b

  def maxScore(nums: Array[Int]): Long = {
    val n = nums.length
    var gcdAll = nums(0)
    var lcmAll = nums(0)
    var i = 1
    while (i < n) {
      gcdAll = gcd(gcdAll, nums(i))
      lcmAll = lcm(lcmAll, nums(i))
      i += 1
    }
    var ans = gcdAll.toLong * lcmAll
    var skip = 0
    while (skip < n) {
      var g = 0
      var l = 1
      var first = true
      i = 0
      while (i < n) {
        if (i != skip) {
          if (first) { g = nums(i); l = nums(i); first = false }
          else { g = gcd(g, nums(i)); l = lcm(l, nums(i)) }
        }
        i += 1
      }
      if (!first) {
        val v = g.toLong * l
        if (v > ans) ans = v
      }
      skip += 1
    }
    ans
  }
}
