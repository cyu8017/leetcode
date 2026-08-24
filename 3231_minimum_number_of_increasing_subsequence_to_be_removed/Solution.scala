// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val g = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (x <- nums) {
      var l = 0
      var r = g.length
      while (l < r) {
        val mid = (l + r) >> 1
        if (g(mid) < x) r = mid else l = mid + 1
      }
      if (l == g.length) g += x else g(l) = x
    }
    g.length
  }
}
