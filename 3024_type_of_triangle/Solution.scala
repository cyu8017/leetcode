// LeetCode 3024 - Type of Triangle
// https://leetcode.com/problems/type-of-triangle/

object Solution {
  def triangleType(nums: Array[Int]): String = {
    scala.util.Sorting.quickSort(nums)
    if (nums(0) + nums(1) <= nums(2)) "none"
    else if (nums(0) == nums(2)) "equilateral"
    else if (nums(0) == nums(1) || nums(1) == nums(2)) "isosceles"
    else "scalene"
  }
}
