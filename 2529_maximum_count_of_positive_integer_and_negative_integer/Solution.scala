// LeetCode 2529 - Maximum Count of Positive Integer and Negative Integer
// https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

object Solution {
  def maximumCount(nums: Array[Int]): Int = {
    var pos = 0
    var neg = 0
    nums.foreach { x =>
      if (x > 0) pos += 1
      else if (x < 0) neg += 1
    }
    math.max(pos, neg)
  }
}
