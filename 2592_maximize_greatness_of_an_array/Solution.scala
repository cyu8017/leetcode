// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

object Solution {
  def maximizeGreatness(nums: Array[Int]): Int = {
    java.util.Arrays.sort(nums)
    var i = 0
    nums.foreach { x =>
      if (x > nums(i)) i += 1
    }
    i
  }
}
