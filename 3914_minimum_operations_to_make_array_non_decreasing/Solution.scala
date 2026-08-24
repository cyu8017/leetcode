// LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

object Solution {
  def minOperations(nums: Array[Int]): Long = {
    var ans = 0L
    var i = 1
    while (i < nums.length) {
      ans += math.max(0L, nums(i - 1).toLong - nums(i))
      i += 1
    }
    ans
  }
}
