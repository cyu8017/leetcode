// LeetCode 0704 - Binary Search
// https://leetcode.com/problems/binary-search/

object Solution {
  def search(nums: Array[Int], target: Int): Int = {
    var left = 0
    var right = nums.length - 1
    while (left <= right) {
      val mid = left + (right - left) / 2
      if (nums(mid) == target) return mid
      if (nums(mid) < target) left = mid + 1
      else right = mid - 1
    }
    -1
  }
}
