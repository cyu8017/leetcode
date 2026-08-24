// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

object Solution {
  def countAlternatingSubarrays(nums: Array[Int]): Long = {
    var ans = 1L
    var s = 1L
    var i = 1
    while (i < nums.length) {
      if (nums(i) != nums(i - 1)) s += 1
      else s = 1
      ans += s
      i += 1
    }
    ans
  }
}
