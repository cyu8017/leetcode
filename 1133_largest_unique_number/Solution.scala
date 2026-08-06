// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

object Solution {
  def largestUniqueNumber(nums: Array[Int]): Int = {
    val count = nums.groupBy(identity).view.mapValues(_.length).toMap
    nums.filter(x => count(x) == 1).foldLeft(-1)(math.max)
  }
}
