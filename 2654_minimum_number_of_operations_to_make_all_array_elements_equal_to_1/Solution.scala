// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val n = nums.length
    var ones = 0
    var i = 0
    while (i < n) {
      if (nums(i) == 1) ones += 1
      i += 1
    }
    if (ones > 0) return n - ones
    var best = n + 1
    i = 0
    while (i < n) {
      var g = 0
      var j = i
      var done = false
      while (j < n && !done) {
        g = gcd(g, nums(j))
        if (g == 1) {
          best = math.min(best, j - i)
          done = true
        }
        j += 1
      }
      i += 1
    }
    if (best == n + 1) -1 else best + n - 1
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
}
