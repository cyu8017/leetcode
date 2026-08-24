// LeetCode 0896 - Monotonic Array
// https://leetcode.com/problems/monotonic-array/

object Solution {
  def isMonotonic(nums: Array[Int]): Boolean = {
    var inc = true
    var dec = true
    var i = 1
    while (i < nums.length) {
      if (nums(i) < nums(i - 1)) inc = false
      if (nums(i) > nums(i - 1)) dec = false
      i += 1
    }
    inc || dec
  }
}
