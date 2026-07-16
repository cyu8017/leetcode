// LeetCode 0128 - Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

object Solution {
  def longestConsecutive(nums: Array[Int]): Int = {
    val values = nums.toSet
    var best = 0
    for (num <- values if !values.contains(num - 1)) {
      var length = 1
      while (values.contains(num + length)) length += 1
      best = Math.max(best, length)
    }
    best
  }
}