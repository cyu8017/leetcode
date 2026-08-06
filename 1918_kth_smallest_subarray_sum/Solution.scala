// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

object Solution {
  def kthSmallestSubarraySum(nums: Array[Int], k: Int): Int = {
    def count(limit: Int): Int = {
      var total = 0
      var left = 0
      var ans = 0
      for (right <- nums.indices) {
        total += nums(right)
        while (total > limit) {
          total -= nums(left)
          left += 1
        }
        ans += right - left + 1
      }
      ans
    }
    var lo = nums.min
    var hi = nums.sum
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (count(mid) >= k) hi = mid
      else lo = mid + 1
    }
    lo
  }
}
