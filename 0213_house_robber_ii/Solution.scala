// LeetCode 0213 - House Robber II
// https://leetcode.com/problems/house-robber-ii/

object Solution {
  def rob(nums: Array[Int]): Int = {
    if (nums.length == 1) return nums(0)
    math.max(robLinear(nums, 0, nums.length - 1), robLinear(nums, 1, nums.length))
  }

  private def robLinear(nums: Array[Int], start: Int, end: Int): Int = {
    var previousTwo = 0
    var previousOne = 0
    for (i <- start until end) {
      val current = math.max(previousOne, previousTwo + nums(i))
      previousTwo = previousOne
      previousOne = current
    }
    previousOne
  }
}
