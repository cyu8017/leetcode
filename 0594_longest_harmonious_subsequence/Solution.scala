// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/

import scala.collection.mutable

object Solution {
  def findLHS(nums: Array[Int]): Int = {
    val counts = mutable.Map.empty[Int, Int]
    nums.foreach(num => counts(num) = counts.getOrElse(num, 0) + 1)
    var best = 0
    counts.foreach { case (key, value) =>
      counts.get(key + 1).foreach { nxt =>
        best = math.max(best, value + nxt)
      }
    }
    best
  }
}
