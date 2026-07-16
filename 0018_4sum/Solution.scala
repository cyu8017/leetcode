// LeetCode 0018 - 4Sum
// https://leetcode.com/problems/4sum/

object Solution {
  def fourSum(nums: Array[Int], target: Int): List[List[Int]] = {
    val sorted = nums.sorted
    val result = scala.collection.mutable.ListBuffer.empty[List[Int]]

    var i = 0
    while (i < sorted.length - 3) {
      if (i > 0 && sorted(i) == sorted(i - 1)) {
        i += 1
      } else {
        var j = i + 1
        while (j < sorted.length - 2) {
          if (j > i + 1 && sorted(j) == sorted(j - 1)) {
            j += 1
          } else {
            var left = j + 1
            var right = sorted.length - 1
            while (left < right) {
              val total = sorted(i).toLong + sorted(j) + sorted(left) + sorted(right)
              if (total == target) {
                result += List(sorted(i), sorted(j), sorted(left), sorted(right))
                while (left < right && sorted(left) == sorted(left + 1)) {
                  left += 1
                }
                while (left < right && sorted(right) == sorted(right - 1)) {
                  right -= 1
                }
                left += 1
                right -= 1
              } else if (total < target) {
                left += 1
              } else {
                right -= 1
              }
            }
            j += 1
          }
        }
        i += 1
      }
    }

    result.toList
  }
}
