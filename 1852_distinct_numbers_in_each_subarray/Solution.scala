// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

import scala.collection.mutable

object Solution {
  def distinctNumbers(nums: Array[Int], k: Int): Array[Int] = {
    val counts = mutable.Map.empty[Int, Int]
    for (i <- 0 until k) {
      counts(nums(i)) = counts.getOrElse(nums(i), 0) + 1
    }
    val result = mutable.ArrayBuffer(counts.size)
    var left = 0
    for (right <- k until nums.length) {
      counts(nums(right)) = counts.getOrElse(nums(right), 0) + 1
      val outgoing = nums(left)
      counts(outgoing) = counts(outgoing) - 1
      if (counts(outgoing) == 0) counts.remove(outgoing)
      left += 1
      result += counts.size
    }
    result.toArray
  }
}
