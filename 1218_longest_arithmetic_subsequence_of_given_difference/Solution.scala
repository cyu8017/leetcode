// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

object Solution {
  def longestSubsequence(arr: Array[Int], difference: Int): Int = {
    val dp = scala.collection.mutable.Map.empty[Int, Int]
    for (x <- arr) dp(x) = dp.getOrElse(x - difference, 0) + 1
    dp.values.max
  }
}
