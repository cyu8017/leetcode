// LeetCode 2570 - Merge Two 2D Arrays by Summing Values
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

object Solution {
  def mergeArrays(nums1: Array[Array[Int]], nums2: Array[Array[Int]]): Array[Array[Int]] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    var j = 0
    while (i < nums1.length && j < nums2.length) {
      if (nums1(i)(0) == nums2(j)(0)) {
        ans += Array(nums1(i)(0), nums1(i)(1) + nums2(j)(1))
        i += 1
        j += 1
      } else if (nums1(i)(0) < nums2(j)(0)) {
        ans += Array(nums1(i)(0), nums1(i)(1))
        i += 1
      } else {
        ans += Array(nums2(j)(0), nums2(j)(1))
        j += 1
      }
    }
    while (i < nums1.length) {
      ans += Array(nums1(i)(0), nums1(i)(1))
      i += 1
    }
    while (j < nums2.length) {
      ans += Array(nums2(j)(0), nums2(j)(1))
      j += 1
    }
    ans.toArray
  }
}
