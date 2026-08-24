// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

object Solution {
  def numSubarrayBoundedMax(nums: Array[Int], left: Int, right: Int): Int = {
    def countAtMost(bound: Int): Int = {
      var ans = 0
      var cur = 0
      nums.foreach { num =>
        if (num <= bound) {
          cur += 1
          ans += cur
        } else cur = 0
      }
      ans
    }
    countAtMost(right) - countAtMost(left - 1)
  }
}
