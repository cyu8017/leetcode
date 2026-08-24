// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

object Solution {
  private def smallestProperDivisor(x: Int): Int = {
    var d = 2
    while (d * d <= x) {
      if (x % d == 0) return d
      d += 1
    }
    x
  }

  def minOperations(nums: Array[Int]): Int = {
    var ops = 0
    var i = nums.length - 2
    while (i >= 0) {
      if (nums(i) > nums(i + 1)) {
        while (nums(i) > nums(i + 1)) {
          val d = smallestProperDivisor(nums(i))
          if (d == nums(i)) return -1
          nums(i) /= d
          ops += 1
          if (nums(i) > nums(i + 1) && smallestProperDivisor(nums(i)) == nums(i)) return -1
        }
      }
      i -= 1
    }
    ops
  }
}
