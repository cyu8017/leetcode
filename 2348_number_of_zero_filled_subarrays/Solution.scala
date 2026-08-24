// LeetCode 2348 - Number of Zero-Filled Subarrays
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

object Solution {
  def zeroFilledSubarray(nums: Array[Int]): Long = {
    var ans = 0L
    var streak = 0L
    nums.foreach { x =>
      if (x == 0) {
        streak += 1
        ans += streak
      } else streak = 0
    }
    ans
  }
}
