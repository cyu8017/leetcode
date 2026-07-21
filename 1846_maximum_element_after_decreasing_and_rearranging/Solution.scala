// LeetCode 1846 - Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

object Solution {
  def maximumElementAfterDecrementingAndRearranging(arr: Array[Int]): Int = {
    val a = arr.sorted
    a(0) = 1
    for (i <- 1 until a.length) a(i) = math.min(a(i), a(i - 1) + 1)
    a.max
  }
}
