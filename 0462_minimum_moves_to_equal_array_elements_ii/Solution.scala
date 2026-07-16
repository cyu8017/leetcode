// LeetCode 0462 - Minimum Moves to Equal Array Elements II
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

object Solution {
  def minMoves2(nums: Array[Int]): Int = {
    val sorted = nums.sorted
    val median = sorted(sorted.length / 2)
    nums.map(value => math.abs(value - median)).sum
  }
}
