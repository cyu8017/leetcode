// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

object Solution {
  def absDifference(nums: Array[Int], k: Int): Int = {
    java.util.Arrays.sort(nums)
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < k) {
      ans += nums(n - i - 1) - nums(i)
      i += 1
    }
    ans
  }
}
