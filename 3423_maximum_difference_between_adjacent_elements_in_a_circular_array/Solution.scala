// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

object Solution {
  def maxAdjacentDistance(nums: Array[Int]): Int = {
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < n) {
      val d = math.abs(nums(i) - nums((i + 1) % n))
      if (d > ans) ans = d
      i += 1
    }
    ans
  }
}
