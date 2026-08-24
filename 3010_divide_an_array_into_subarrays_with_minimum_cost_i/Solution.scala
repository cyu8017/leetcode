// LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

object Solution {
  def minimumCost(nums: Array[Int]): Int = {
    val a = nums(0)
    var b = 100
    var c = 100
    var i = 1
    while (i < nums.length) {
      val x = nums(i)
      if (x < b) { c = b; b = x }
      else if (x < c) c = x
      i += 1
    }
    a + b + c
  }
}
