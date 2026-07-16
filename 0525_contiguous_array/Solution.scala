// LeetCode 0525 - Contiguous Array
// https://leetcode.com/problems/contiguous-array/

import scala.collection.mutable

object Solution {
  def findMaxLength(nums: Array[Int]): Int = {
    val counts = mutable.Map(0 -> -1)
    var balance = 0
    var best = 0
    for ((num, index) <- nums.zipWithIndex) {
      balance += if (num == 1) 1 else -1
      counts.get(balance) match {
        case Some(previous) => best = math.max(best, index - previous)
        case None           => counts(balance) = index
      }
    }
    best
  }
}
