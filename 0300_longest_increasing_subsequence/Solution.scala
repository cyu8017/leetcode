// LeetCode 0300 - Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

import scala.collection.mutable

object Solution {
  def lengthOfLIS(nums: Array[Int]): Int = {
    val piles = mutable.ArrayBuffer.empty[Int]
    nums.foreach { num =>
      var left = 0
      var right = piles.length
      while (left < right) {
        val mid = (left + right) / 2
        if (piles(mid) < num) {
          left = mid + 1
        } else {
          right = mid
        }
      }
      if (left == piles.length) {
        piles += num
      } else {
        piles(left) = num
      }
    }
    piles.length
  }
}
