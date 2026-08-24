// LeetCode 0659 - Split Array into Consecutive Subsequences
// https://leetcode.com/problems/split-array-into-consecutive-subsequences/

import scala.collection.mutable

object Solution {
  def isPossible(nums: Array[Int]): Boolean = {
    val freq = mutable.Map.empty[Int, Int]
    val tails = mutable.Map.empty[Int, Int]
    nums.foreach(num => freq(num) = freq.getOrElse(num, 0) + 1)
    nums.foreach { num =>
      if (freq.getOrElse(num, 0) != 0) {
        freq(num) = freq(num) - 1
        if (tails.getOrElse(num - 1, 0) > 0) {
          tails(num - 1) = tails(num - 1) - 1
          tails(num) = tails.getOrElse(num, 0) + 1
        } else if (freq.getOrElse(num + 1, 0) > 0 && freq.getOrElse(num + 2, 0) > 0) {
          freq(num + 1) = freq(num + 1) - 1
          freq(num + 2) = freq(num + 2) - 1
          tails(num + 2) = tails.getOrElse(num + 2, 0) + 1
        } else {
          return false
        }
      }
    }
    true
  }
}
