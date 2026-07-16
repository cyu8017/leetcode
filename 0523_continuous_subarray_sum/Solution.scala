// LeetCode 0523 - Continuous Subarray Sum
// https://leetcode.com/problems/continuous-subarray-sum/

import scala.collection.mutable

object Solution {
  def checkSubarraySum(nums: Array[Int], k: Int): Boolean = {
    val remainders = mutable.Map(0 -> -1)
    var prefix = 0
    for ((num, index) <- nums.zipWithIndex) {
      prefix += num
      val mod = if (k != 0) prefix % k else prefix
      remainders.get(mod) match {
        case Some(previous) if index - previous >= 2 => return true
        case None                                    => remainders(mod) = index
        case _                                       =>
      }
    }
    false
  }
}
