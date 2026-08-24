// LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

object Solution {
  def longestSubsequence(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 1
    val dp = Array.fill(n, 301)(0)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < i) {
        val d = math.abs(nums(i) - nums(j))
        var best = 1
        var pd = d
        while (pd <= 300) {
          if (dp(j)(pd) > best) best = dp(j)(pd)
          pd += 1
        }
        if (best + 1 > dp(i)(d)) dp(i)(d) = best + 1
        if (dp(i)(d) > ans) ans = dp(i)(d)
        j += 1
      }
      if (dp(i)(0) < 1) dp(i)(0) = 1
      i += 1
    }
    ans
  }
}
