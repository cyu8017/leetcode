// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

object Solution {
  def minOperations(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length
    var ans = calc(nums1, nums2)
    val t = nums1(n - 1)
    nums1(n - 1) = nums2(n - 1)
    nums2(n - 1) = t
    val cand = calc(nums1, nums2) + 1
    if (cand < ans) ans = cand
    if (ans >= (1 << 30)) -1 else ans
  }

  private def calc(a1: Array[Int], a2: Array[Int]): Int = {
    val n = a1.length
    var ops = 0
    val last1 = a1(n - 1)
    val last2 = a2(n - 1)
    for (i <- 0 until n - 1) {
      val x = a1(i)
      val y = a2(i)
      if (x <= last1 && y <= last2) {}
      else if (y <= last1 && x <= last2) ops += 1
      else return 1 << 30
    }
    ops
  }
}
