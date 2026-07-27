// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

object Solution {
  def maximumUniqueSubarray(nums: Array[Int]): Int = {
    val seen = scala.collection.mutable.Map.empty[Int, Int]
    var left = 0
    var cur = 0
    var best = 0
    for (right <- nums.indices) {
      val x = nums(right)
      if (seen.contains(x) && seen(x) >= left) {
        while (left <= seen(x)) {
          cur -= nums(left)
          left += 1
        }
      }
      seen(x) = right
      cur += x
      if (cur > best) best = cur
    }
    best
  }
}
