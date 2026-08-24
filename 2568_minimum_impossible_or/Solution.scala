// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

object Solution {
  def minImpossibleOR(nums: Array[Int]): Int = {
    val set = nums.toSet
    var x = 1
    while (set.contains(x)) x <<= 1
    x
  }
}
