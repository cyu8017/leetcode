// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

object Solution {
  def minSum(nums1: Array[Int], nums2: Array[Int]): Long = {
    var s1 = 0L
    var s2 = 0L
    var z1 = 0
    var z2 = 0
    nums1.foreach { v =>
      if (v == 0) {
        z1 += 1
        s1 += 1
      } else s1 += v
    }
    nums2.foreach { v =>
      if (v == 0) {
        z2 += 1
        s2 += 1
      } else s2 += v
    }
    if (z1 == 0 && s1 < s2) return -1
    if (z2 == 0 && s2 < s1) return -1
    if (s1 > s2) s1 else s2
  }
}
