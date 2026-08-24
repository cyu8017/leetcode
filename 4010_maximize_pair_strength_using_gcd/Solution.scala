// LeetCode 4010 - Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/

object Solution {
  private def gcd(a0: Long, b0: Long): Long = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def maxPairStrength(nums: Array[Int]): Long = {
    val n = nums.length
    var ans = 0L
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val g = gcd(nums(i), nums(j))
        val x = nums(i).toLong * nums(j) / (g * g)
        ans = math.max(ans, x)
        j += 1
      }
      i += 1
    }
    ans
  }
}
