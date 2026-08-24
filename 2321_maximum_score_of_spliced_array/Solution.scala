// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

object Solution {
  def maximumsSplicedArray(nums1: Array[Int], nums2: Array[Int]): Int = {
    math.max(kadane(nums1, nums2), kadane(nums2, nums1))
  }

  private def kadane(a: Array[Int], b: Array[Int]): Int = {
    var best = 0
    var cur = 0
    var sum = 0
    var i = 0
    while (i < a.length) {
      sum += a(i)
      cur += b(i) - a(i)
      if (cur < 0) cur = 0
      best = math.max(best, cur)
      i += 1
    }
    sum + best
  }
}
