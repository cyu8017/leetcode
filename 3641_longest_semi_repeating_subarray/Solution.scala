// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

object Solution {
  def longestSubarray(nums: Array[Int], k: Int): Int = {
    val cnt = new java.util.HashMap[Integer, Integer]()
    var ans = 0
    var cur = 0
    var l = 0
    var r = 0
    while (r < nums.length) {
      if (cnt.merge(nums(r), 1, Integer.sum) == 2) cur += 1
      while (cur > k) {
        if (cnt.merge(nums(l), -1, Integer.sum) == 1) cur -= 1
        l += 1
      }
      ans = math.max(ans, r - l + 1)
      r += 1
    }
    ans
  }
}
