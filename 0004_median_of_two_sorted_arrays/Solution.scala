// LeetCode 0004 - Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/

object Solution {
  def findMedianSortedArrays(nums1: Array[Int], nums2: Array[Int]): Double = {
    var a = nums1
    var b = nums2
    if (a.length > b.length) {
      val tmp = a
      a = b
      b = tmp
    }

    val m = a.length
    val n = b.length
    val totalLeft = (m + n + 1) / 2
    var lo = 0
    var hi = m

    while (lo <= hi) {
      val i = (lo + hi) / 2
      val j = totalLeft - i

      val nums1LeftMax = if (i == 0) Int.MinValue else a(i - 1)
      val nums1RightMin = if (i == m) Int.MaxValue else a(i)
      val nums2LeftMax = if (j == 0) Int.MinValue else b(j - 1)
      val nums2RightMin = if (j == n) Int.MaxValue else b(j)

      if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
        return if ((m + n) % 2 == 1) {
          math.max(nums1LeftMax, nums2LeftMax).toDouble
        } else {
          (math.max(nums1LeftMax, nums2LeftMax) + math.min(nums1RightMin, nums2RightMin)) / 2.0
        }
      }

      if (nums1LeftMax > nums2RightMin) hi = i - 1
      else lo = i + 1
    }

    0.0
  }
}
