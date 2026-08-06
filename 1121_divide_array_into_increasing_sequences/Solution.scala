// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

object Solution {
  def canDivideIntoSubsequences(nums: Array[Int], k: Int): Boolean = {
    var maxFreq = 1
    var cur = 1
    for (i <- 1 until nums.length) {
      if (nums(i) == nums(i - 1)) {
        cur += 1
        maxFreq = math.max(maxFreq, cur)
      } else cur = 1
    }
    maxFreq.toLong * k <= nums.length
  }
}
