// LeetCode 1537 - Get the Maximum Score
// https://leetcode.com/problems/get-the-maximum-score/

object Solution {
  def maxSum(nums1: Array[Int], nums2: Array[Int]): Int = {
    var i = 0
    var j = 0
    var first = 0L
    var second = 0L
    while (i < nums1.length || j < nums2.length) {
      if (j == nums2.length || (i < nums1.length && nums1(i) < nums2(j))) {
        first += nums1(i); i += 1
      } else if (i == nums1.length || nums2(j) < nums1(i)) {
        second += nums2(j); j += 1
      } else {
        first = math.max(first, second) + nums1(i)
        second = first
        i += 1; j += 1
      }
    }
    (math.max(first, second) % 1000000007L).toInt
  }
}
