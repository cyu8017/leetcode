// LeetCode 2567 - Minimum Score by Changing Two Elements
// https://leetcode.com/problems/minimum-score-by-changing-two-elements/

object Solution {
  def minimizeSum(nums: Array[Int]): Int = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    val a = nums(n - 1) - nums(2)
    val b = nums(n - 3) - nums(0)
    val c = nums(n - 2) - nums(1)
    math.min(a, math.min(b, c))
  }
}
