// LeetCode 0665 - Non-decreasing Array
// https://leetcode.com/problems/non-decreasing-array/

object Solution {
  def checkPossibility(nums: Array[Int]): Boolean = {
    var changed = false
    var i = 1
    while (i < nums.length) {
      if (nums(i) < nums(i - 1)) {
        if (changed) return false
        changed = true
        if (i >= 2 && nums(i) < nums(i - 2)) nums(i) = nums(i - 1)
        else nums(i - 1) = nums(i)
      }
      i += 1
    }
    true
  }
}
