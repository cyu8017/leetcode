// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

object Solution {
  def findLength(nums1: Array[Int], nums2: Array[Int]): Int = {
    val m = nums1.length
    val n = nums2.length
    var best = 0
    var dp = Array.fill(n + 1)(0)
    var i = 1
    while (i <= m) {
      val next = Array.fill(n + 1)(0)
      var j = 1
      while (j <= n) {
        if (nums1(i - 1) == nums2(j - 1)) {
          next(j) = dp(j - 1) + 1
          best = math.max(best, next(j))
        }
        j += 1
      }
      dp = next
      i += 1
    }
    best
  }
}
