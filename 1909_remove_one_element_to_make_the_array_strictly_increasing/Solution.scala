// LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

object Solution {
  def canBeIncreasing(nums: Array[Int]): Boolean = {
    def check(skip: Int): Boolean = {
      var prev = Int.MinValue
      var first = true
      for (i <- nums.indices if i != skip) {
        if (!first && nums(i) <= prev) return false
        prev = nums(i)
        first = false
      }
      true
    }
    for (i <- 1 until nums.length) {
      if (nums(i) <= nums(i - 1)) return check(i - 1) || check(i)
    }
    true
  }
}
