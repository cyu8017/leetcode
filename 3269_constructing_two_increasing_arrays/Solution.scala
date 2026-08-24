// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

object Solution {
  def minLargest(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length
    val m = nums2.length
    val inf = 1000000000
    val dp = Array.fill(n + 1, m + 1)(inf)
    dp(0)(0) = 0
    var i = 0
    while (i <= n) {
      var j = 0
      while (j <= m) {
        if (dp(i)(j) != inf) {
          val prev = dp(i)(j)
          if (i < n) {
            var need = prev + 1
            if (nums1(i) == 0) { if (need % 2 != 0) need += 1 }
            else { if (need % 2 == 0) need += 1 }
            if (need < dp(i + 1)(j)) dp(i + 1)(j) = need
          }
          if (j < m) {
            var need = prev + 1
            if (nums2(j) == 0) { if (need % 2 != 0) need += 1 }
            else { if (need % 2 == 0) need += 1 }
            if (need < dp(i)(j + 1)) dp(i)(j + 1) = need
          }
        }
        j += 1
      }
      i += 1
    }
    dp(n)(m)
  }
}
