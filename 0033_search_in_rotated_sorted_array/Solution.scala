// LeetCode 0033 - Search in Rotated Sorted Array
// https://leetcode.com/problems/search-in-rotated-sorted-array/

object Solution {
  def search(nums: Array[Int], target: Int): Int = {
    var left = 0
    var right = nums.length - 1

    while (left <= right) {
      val mid = (left + right) / 2
      if (nums(mid) == target) {
        return mid
      }

      if (nums(left) <= nums(mid)) {
        if (nums(left) <= target && target < nums(mid)) {
          right = mid - 1
        } else {
          left = mid + 1
        }
      } else {
        if (nums(mid) < target && target <= nums(right)) {
          left = mid + 1
        } else {
          right = mid - 1
        }
      }
    }

    -1
  }
}
