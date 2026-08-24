// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

object Solution {
  def missingInteger(nums: Array[Int]): Int = {
    var sum = nums(0)
    var i = 1
    while (i < nums.length && nums(i) == nums(i - 1) + 1) {
      sum += nums(i)
      i += 1
    }
    val seen = nums.toSet
    while (seen.contains(sum)) sum += 1
    sum
  }
}
