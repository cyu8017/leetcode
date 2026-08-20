// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

object Solution {
  def findSpecialInteger(arr: Array[Int]): Int = {
    val n = arr.length
    for (value <- Seq(arr(n / 4), arr(n / 2), arr(3 * n / 4))) {
      if (arr.count(_ == value) > n / 4) return value
    }
    arr(0)
  }
}
