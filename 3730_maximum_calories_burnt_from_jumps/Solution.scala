// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

object Solution {
  def maxCaloriesBurnt(heights: Array[Int]): Long = {
    java.util.Arrays.sort(heights)
    var ans = 0L
    var pre = 0
    var l = 0
    var r = heights.length - 1
    while (l < r) {
      val d1 = heights(r).toLong - pre
      ans += d1 * d1
      val d2 = heights(l).toLong - heights(r)
      ans += d2 * d2
      pre = heights(l)
      l += 1
      r -= 1
    }
    val d = heights(r).toLong - pre
    ans += d * d
    ans
  }
}
