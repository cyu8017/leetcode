// LeetCode 0088 - Merge Sorted Array
// https://leetcode.com/problems/merge-sorted-array/

object Solution {
  def merge(nums1: Array[Int], m: Int, nums2: Array[Int], n: Int): Unit = {
    var i = m - 1
    var j = n - 1
    var write = m + n - 1

    while (j >= 0) {
      if (i >= 0 && nums1(i) > nums2(j)) {
        nums1(write) = nums1(i)
        i -= 1
      } else {
        nums1(write) = nums2(j)
        j -= 1
      }
      write -= 1
    }
  }
}
