// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

object Solution {
  def kthSmallestProduct(nums1: Array[Int], nums2: Array[Int], k: Long): Long = {
    def countLE(x: Long): Long = {
      var cnt = 0L
      nums1.foreach { a =>
        if (a > 0) {
          var lo = 0
          var hi = nums2.length
          while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a.toLong * nums2(mid) <= x) lo = mid + 1
            else hi = mid
          }
          cnt += lo
        } else if (a < 0) {
          var lo = 0
          var hi = nums2.length
          while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a.toLong * nums2(mid) <= x) hi = mid
            else lo = mid + 1
          }
          cnt += nums2.length - lo
        } else if (x >= 0) cnt += nums2.length
      }
      cnt
    }
    var lo = -10000000000L
    var hi = 10000000000L
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (countLE(mid) >= k) hi = mid
      else lo = mid + 1
    }
    lo
  }
}
