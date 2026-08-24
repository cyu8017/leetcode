// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

object Solution {
  def findNonMinOrMax(nums: Array[Int]): Int = {
    if (nums.length < 3) return -1
    val a = nums(0)
    val b = nums(1)
    val c = nums(2)
    a + b + c - math.max(a, math.max(b, c)) - math.min(a, math.min(b, c))
  }
}
