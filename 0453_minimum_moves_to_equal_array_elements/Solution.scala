// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

object Solution {
  def minMoves(nums: Array[Int]): Int = {
    val minimum = nums.min
    nums.map(_ - minimum).sum
  }
}
