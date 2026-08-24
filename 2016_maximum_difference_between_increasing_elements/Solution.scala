// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

object Solution {
  def maximumDifference(nums: Array[Int]): Int = {
    var ans = -1
    var mn = nums(0)
    var i = 1
    while (i < nums.length) {
      if (nums(i) > mn) ans = math.max(ans, nums(i) - mn)
      else mn = nums(i)
      i += 1
    }
    ans
  }
}
