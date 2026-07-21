// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

object Solution {
  def minProductSum(nums1: Array[Int], nums2: Array[Int]): Int = {
    val a = nums1.sorted
    val b = nums2.sorted.reverse
    a.zip(b).map { case (x, y) => x * y }.sum
  }
}
