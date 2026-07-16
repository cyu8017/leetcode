// LeetCode 0015 - 3Sum
// https://leetcode.com/problems/3sum/

object Solution {
  def threeSum(nums: Array[Int]): List[List[Int]] = {
    val sorted = nums.sorted
    val result = scala.collection.mutable.ListBuffer.empty[List[Int]]

    var i = 0
    while (i < sorted.length - 2) {
      if (i > 0 && sorted(i) == sorted(i - 1)) {
        i += 1
      } else {
        var left = i + 1
        var right = sorted.length - 1
        while (left < right) {
          val total = sorted(i) + sorted(left) + sorted(right)
          if (total == 0) {
            result += List(sorted(i), sorted(left), sorted(right))
            while (left < right && sorted(left) == sorted(left + 1)) {
              left += 1
            }
            while (left < right && sorted(right) == sorted(right - 1)) {
              right -= 1
            }
            left += 1
            right -= 1
          } else if (total < 0) {
            left += 1
          } else {
            right -= 1
          }
        }
        i += 1
      }
    }

    result.toList
  }
}
