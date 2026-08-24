// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

object Solution {
  def findLengthOfLCIS(nums: Array[Int]): Int = {
    var best = 1
    var cur = 1
    var i = 1
    while (i < nums.length) {
      if (nums(i) > nums(i - 1)) {
        cur += 1
        best = math.max(best, cur)
      } else {
        cur = 1
      }
      i += 1
    }
    best
  }
}
