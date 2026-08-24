// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

object Solution {
  def maximizeSum(nums: Array[Int], k: Int): Int = {
    var mx = nums(0)
    var i = 0
    while (i < nums.length) {
      if (nums(i) > mx) mx = nums(i)
      i += 1
    }
    k * mx + k * (k - 1) / 2
  }
}
