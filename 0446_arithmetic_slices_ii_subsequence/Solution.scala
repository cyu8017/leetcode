// LeetCode 0446 - Arithmetic Slices II - Subsequence
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

import scala.collection.mutable

object Solution {
  def numberOfArithmeticSlices(nums: Array[Int]): Int = {
    var total = 0
    val differences = Array.fill(nums.length)(mutable.Map.empty[Int, Int])

    for (index <- nums.indices) {
      val value = nums(index)
      for (previous <- 0 until index) {
        val diff = value - nums(previous)
        total += differences(previous).getOrElse(diff, 0)
        differences(index)(diff) = differences(index).getOrElse(diff, 0) + differences(previous).getOrElse(diff, 0) + 1
      }
    }

    total
  }
}
