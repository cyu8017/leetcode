// LeetCode 0976 - Largest Perimeter Triangle
// https://leetcode.com/problems/largest-perimeter-triangle/

object Solution {
  def largestPerimeter(nums: Array[Int]): Int = {
    val arr = nums.sorted
    var i = arr.length - 1
    while (i >= 2) {
      if (arr(i) < arr(i - 1) + arr(i - 2))
        return arr(i) + arr(i - 1) + arr(i - 2)
      i -= 1
    }
    0
  }
}
