// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

object Solution {
  def lengthOfLongestSubsequence(nums: Array[Int], target: Int): Int = {
    val dp = Array.fill(target + 1)(-1)
    dp(0) = 0
    nums.foreach { v =>
      var s = target
      while (s >= v) {
        if (dp(s - v) >= 0 && dp(s - v) + 1 > dp(s)) dp(s) = dp(s - v) + 1
        s -= 1
      }
    }
    dp(target)
  }
}
