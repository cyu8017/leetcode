// LeetCode 0034 - Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

object Solution {
  def searchRange(nums: Array[Int], target: Int): Array[Int] = {
    if (nums.isEmpty) {
      return Array(-1, -1)
    }

    val start = lowerBound(nums, target)
    if (start == nums.length || nums(start) != target) {
      return Array(-1, -1)
    }

    Array(start, upperBound(nums, target) - 1)
  }

  private def lowerBound(nums: Array[Int], target: Int): Int = {
    var left = 0
    var right = nums.length

    while (left < right) {
      val mid = (left + right) / 2
      if (nums(mid) < target) {
        left = mid + 1
      } else {
        right = mid
      }
    }

    left
  }

  private def upperBound(nums: Array[Int], target: Int): Int = {
    var left = 0
    var right = nums.length

    while (left < right) {
      val mid = (left + right) / 2
      if (nums(mid) <= target) {
        left = mid + 1
      } else {
        right = mid
      }
    }

    left
  }
}
