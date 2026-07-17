// LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

object Solution {
  def minOperations(nums1: Array[Int], nums2: Array[Int]): Int = {
    if (nums1.length * 6 < nums2.length || nums2.length * 6 < nums1.length) {
      return -1
    }
    var s1 = nums1.sum
    var s2 = nums2.sum
    if (s1 == s2) {
      return 0
    }
    var big = nums1
    var small = nums2
    if (s1 < s2) {
      big = nums2
      small = nums1
      val tmp = s1
      s1 = s2
      s2 = tmp
    }
    var diff = s1 - s2
    val gains = (big.map(_ - 1) ++ small.map(6 - _)).sorted(Ordering.Int.reverse)
    var ops = 0
    var i = 0
    while (i < gains.length && diff > 0) {
      diff -= gains(i)
      ops += 1
      i += 1
    }
    if (diff <= 0) ops else -1
  }
}
