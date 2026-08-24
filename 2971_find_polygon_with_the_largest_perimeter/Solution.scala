// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

object Solution {
  def largestPerimeter(nums: Array[Int]): Long = {
    scala.util.Sorting.quickSort(nums)
    var sum = 0L
    for (v <- nums) sum += v
    var i = nums.length - 1
    while (i >= 2) {
      sum -= nums(i)
      if (sum > nums(i)) return sum + nums(i)
      i -= 1
    }
    -1
  }
}
