// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    val need = scala.collection.mutable.Set((1 to k): _*)
    for (i <- nums.indices.reverse) {
      need.remove(nums(i))
      if (need.isEmpty) return nums.length - i
    }
    nums.length
  }
}
