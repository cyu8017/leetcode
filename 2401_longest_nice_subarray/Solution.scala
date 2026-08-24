// LeetCode 2401 - Longest Nice Subarray
// https://leetcode.com/problems/longest-nice-subarray/

object Solution {
  def longestNiceSubarray(nums: Array[Int]): Int = {
    var used = 0
    var left = 0
    var ans = 0
    var right = 0
    while (right < nums.length) {
      while ((used & nums(right)) != 0) {
        used ^= nums(left)
        left += 1
      }
      used |= nums(right)
      ans = math.max(ans, right - left + 1)
      right += 1
    }
    ans
  }
}
