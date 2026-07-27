// LeetCode 1664 - Ways to Make a Fair Array
// https://leetcode.com/problems/ways-to-make-a-fair-array/

object Solution {
  def waysToMakeFair(nums: Array[Int]): Int = {
    var te = 0
    var to = 0
    for (i <- nums.indices) {
      if (i % 2 == 0) te += nums(i) else to += nums(i)
    }
    var le = 0
    var lo = 0
    var ans = 0
    for (i <- nums.indices) {
      val x = nums(i)
      if (i % 2 == 1) to -= x else te -= x
      if (le + to == lo + te) ans += 1
      if (i % 2 == 1) lo += x else le += x
    }
    ans
  }
}
