// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

object Solution {
  def minimizeArrayValue(nums: Array[Int]): Int = {
    var sum = 0L
    var ans = 0
    var i = 0
    while (i < nums.length) {
      sum += nums(i)
      val avg = ((sum + i) / (i + 1)).toInt
      if (avg > ans) ans = avg
      i += 1
    }
    ans
  }
}
