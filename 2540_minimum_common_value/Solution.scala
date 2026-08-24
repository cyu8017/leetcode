// LeetCode 2540 - Minimum Common Value
// https://leetcode.com/problems/minimum-common-value/

object Solution {
  def getCommon(nums1: Array[Int], nums2: Array[Int]): Int = {
    var i = 0
    var j = 0
    while (i < nums1.length && j < nums2.length) {
      if (nums1(i) == nums2(j)) return nums1(i)
      if (nums1(i) < nums2(j)) i += 1
      else j += 1
    }
    -1
  }
}
