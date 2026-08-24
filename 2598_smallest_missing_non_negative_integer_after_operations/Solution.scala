// LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

object Solution {
  def findSmallestInteger(nums: Array[Int], value: Int): Int = {
    val cnt = Array.fill(value)(0)
    nums.foreach { x =>
      var r = x % value
      if (r < 0) r += value
      cnt(r) += 1
    }
    var mex = 0
    while (cnt(mex % value) > 0) {
      cnt(mex % value) -= 1
      mex += 1
    }
    mex
  }
}
