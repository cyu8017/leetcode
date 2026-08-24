// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

object Solution {
  def maxSubarrays(nums: Array[Int]): Int = {
    var ans = 0
    var cur = -1
    nums.foreach { v =>
      if (cur == -1) cur = v
      else cur &= v
      if (cur == 0) {
        ans += 1
        cur = -1
      }
    }
    if (ans == 0) 1 else ans
  }
}
