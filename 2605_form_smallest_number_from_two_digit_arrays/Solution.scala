// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

object Solution {
  def minNumber(nums1: Array[Int], nums2: Array[Int]): Int = {
    val s1 = nums1.toSet
    val s2 = nums2.toSet
    var common = 10
    s1.foreach { x => if (s2.contains(x) && x < common) common = x }
    if (common < 10) return common
    var a = 10
    var b = 10
    nums1.foreach(x => if (x < a) a = x)
    nums2.foreach(x => if (x < b) b = x)
    math.min(a * 10 + b, b * 10 + a)
  }
}
