// LeetCode 0454 - 4Sum II
// https://leetcode.com/problems/4sum-ii/

import scala.collection.mutable

object Solution {
  def fourSumCount(
      nums1: Array[Int],
      nums2: Array[Int],
      nums3: Array[Int],
      nums4: Array[Int]
  ): Int = {
    val pairSums = mutable.Map.empty[Int, Int]
    for (a <- nums1; b <- nums2) {
      val sum = a + b
      pairSums(sum) = pairSums.getOrElse(sum, 0) + 1
    }

    var total = 0
    for (c <- nums3; d <- nums4) {
      total += pairSums.getOrElse(-(c + d), 0)
    }
    total
  }
}
