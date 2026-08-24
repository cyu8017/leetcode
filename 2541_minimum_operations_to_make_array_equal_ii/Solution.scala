// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

object Solution {
  def minOperations(nums1: Array[Int], nums2: Array[Int], k: Int): Long = {
    if (k == 0) {
      var i = 0
      while (i < nums1.length) {
        if (nums1(i) != nums2(i)) return -1
        i += 1
      }
      return 0
    }
    var pos = 0L
    var neg = 0L
    var i = 0
    while (i < nums1.length) {
      val d = nums1(i) - nums2(i)
      if (d % k != 0) return -1
      if (d > 0) pos += d / k
      else neg += (-d) / k
      i += 1
    }
    if (pos != neg) -1 else pos
  }
}
