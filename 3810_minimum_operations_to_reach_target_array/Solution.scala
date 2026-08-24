// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

object Solution {
  def minOperations(nums: Array[Int], target: Array[Int]): Int = {
    val s = new java.util.HashSet[Integer]()
    var i = 0
    while (i < nums.length) {
      if (nums(i) != target(i)) s.add(nums(i))
      i += 1
    }
    s.size()
  }
}
