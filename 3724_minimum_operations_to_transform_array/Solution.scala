// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

object Solution {
  def minOperations(nums1: Array[Int], nums2: Array[Int]): Long = {
    var ans = 1L
    val n = nums1.length
    var ok = false
    var d = 1 << 30
    var i = 0
    while (i < n) {
      val x = math.max(nums1(i), nums2(i))
      val y = math.min(nums1(i), nums2(i))
      ans += x - y
      d = math.min(d, math.min(math.abs(x - nums2(n)), math.abs(y - nums2(n))))
      if (nums2(n) >= y && nums2(n) <= x) ok = true
      i += 1
    }
    if (!ok) ans += d
    ans
  }
}
