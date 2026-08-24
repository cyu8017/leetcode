// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

object Solution {
  def validSubarraySplit(nums: Array[Int]): Int = {
    def gcd(x: Int, y: Int): Int = {
      var a = x
      var b = y
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    val n = nums.length
    val INF = 1 << 30
    val dp = Array.fill(n + 1)(INF)
    dp(0) = 0
    var i = 0
    while (i < n) {
      if (dp(i) < INF) {
        var j = i
        while (j < n) {
          if (gcd(nums(i), nums(j)) > 1) {
            if (dp(i) + 1 < dp(j + 1)) dp(j + 1) = dp(i) + 1
          }
          j += 1
        }
      }
      i += 1
    }
    if (dp(n) >= INF) -1 else dp(n)
  }
}
