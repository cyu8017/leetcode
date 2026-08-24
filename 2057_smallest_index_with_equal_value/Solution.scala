// LeetCode 2057 - Smallest Index With Equal Value
// https://leetcode.com/problems/smallest-index-with-equal-value/

object Solution {
  def smallestEqual(nums: Array[Int]): Int = {
    var i = 0
    while (i < nums.length) {
      if (i % 10 == nums(i)) return i
      i += 1
    }
    -1
  }
}
