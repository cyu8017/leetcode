// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

object Solution {
  def maxDistance(nums1: Array[Int], nums2: Array[Int]): Int = {
    var answer = 0
    var j = 0
    for (i <- nums1.indices) {
      while (j < nums2.length && nums1(i) <= nums2(j)) {
        j += 1
      }
      answer = math.max(answer, j - i - 1)
    }
    answer
  }
}
