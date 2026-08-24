// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

import scala.collection.mutable

object Solution {
  def subarraySum(nums: Array[Int], k: Int): Int = {
    val counts = mutable.Map[Int, Int](0 -> 1)
    var prefix = 0
    var answer = 0
    nums.foreach { num =>
      prefix += num
      answer += counts.getOrElse(prefix - k, 0)
      counts(prefix) = counts.getOrElse(prefix, 0) + 1
    }
    answer
  }
}
