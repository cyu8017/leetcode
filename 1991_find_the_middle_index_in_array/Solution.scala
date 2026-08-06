// LeetCode 1991 - Find the Middle Index in Array
// https://leetcode.com/problems/find-the-middle-index-in-array/

object Solution {
  def findMiddleIndex(nums: Array[Int]): Int = {
    val total = nums.sum
    var left = 0
    for (i <- nums.indices) {
      if (left == total - left - nums(i)) return i
      left += nums(i)
    }
    -1
  }
}
