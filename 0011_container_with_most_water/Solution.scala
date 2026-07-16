// LeetCode 0011 - Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

object Solution {
  def maxArea(height: Array[Int]): Int = {
    var left = 0
    var right = height.length - 1
    var best = 0

    while (left < right) {
      val width = right - left
      best = math.max(best, math.min(height(left), height(right)) * width)
      if (height(left) < height(right)) left += 1
      else right -= 1
    }

    best
  }
}
