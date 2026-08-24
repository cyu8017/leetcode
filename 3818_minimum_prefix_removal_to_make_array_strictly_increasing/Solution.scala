// LeetCode 3818 - Minimum Prefix Removal To Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

object Solution {
  def minimumPrefixLength(nums: Array[Int]): Int = {
    var i = nums.length - 1
    while (i > 0) {
      if (nums(i - 1) >= nums(i)) return i
      i -= 1
    }
    0
  }
}
