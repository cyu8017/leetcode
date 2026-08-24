// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

object Solution {
  def check(nums: Array[Int], target: Int, kk: Int): Boolean = {
    var cnt = 0
    var sign = 1
    var i = 0
    while (i < nums.length - 1) {
      val x = nums(i) * sign
      if (x == target) sign = 1
      else { sign = -1; cnt += 1 }
      i += 1
    }
    cnt <= kk && nums(nums.length - 1) * sign == target
  }

  def canMakeEqual(nums: Array[Int], k: Int): Boolean =
    check(nums, nums(0), k) || check(nums, -nums(0), k)
}
