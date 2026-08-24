// LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

object Solution {
  def maxNonDecreasingLength(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length
    var dp1 = 1
    var dp2 = 1
    var ans = 1
    var i = 1
    while (i < n) {
      var nd1 = 1
      var nd2 = 1
      if (nums1(i) >= nums1(i - 1)) nd1 = math.max(nd1, dp1 + 1)
      if (nums1(i) >= nums2(i - 1)) nd1 = math.max(nd1, dp2 + 1)
      if (nums2(i) >= nums1(i - 1)) nd2 = math.max(nd2, dp1 + 1)
      if (nums2(i) >= nums2(i - 1)) nd2 = math.max(nd2, dp2 + 1)
      dp1 = nd1
      dp2 = nd2
      ans = math.max(ans, math.max(dp1, dp2))
      i += 1
    }
    ans
  }
}
