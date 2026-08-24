// LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
// https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

object Solution {
  def maximumMatchingIndices(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length
    var ans = 0
    var shift = 0
    while (shift < n) {
      var cnt = 0
      var i = 0
      while (i < n) {
        if (nums1((i - shift + n) % n) == nums2(i)) cnt += 1
        i += 1
      }
      if (cnt > ans) ans = cnt
      shift += 1
    }
    ans
  }
}
