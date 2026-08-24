// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

object Solution {
  def minSwap(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length
    val swap = Array.fill(n)(n)
    val keep = Array.fill(n)(n)
    swap(0) = 1
    keep(0) = 0
    var i = 1
    while (i < n) {
      if (nums1(i) > nums1(i - 1) && nums2(i) > nums2(i - 1)) {
        keep(i) = keep(i - 1)
        swap(i) = swap(i - 1) + 1
      }
      if (nums1(i) > nums2(i - 1) && nums2(i) > nums1(i - 1)) {
        keep(i) = math.min(keep(i), swap(i - 1))
        swap(i) = math.min(swap(i), keep(i - 1) + 1)
      }
      i += 1
    }
    math.min(swap(n - 1), keep(n - 1))
  }
}
