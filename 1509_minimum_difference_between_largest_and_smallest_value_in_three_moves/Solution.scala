// LeetCode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

object Solution {
  def minDifference(nums: Array[Int]): Int = {
    if (nums.length <= 4) return 0
    val a = nums.sorted
    (0 until 4).map(i => a(a.length - 4 + i) - a(i)).min
  }
}
