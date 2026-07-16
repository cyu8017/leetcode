// LeetCode 0259 - 3Sum Smaller
// https://leetcode.com/problems/3sum-smaller/

object Solution {
  def threeSumSmaller(nums: Array[Int], target: Int): Int = {
    val sorted = nums.sorted
    var count = 0
    var index = 0
    while (index < sorted.length - 2) {
      var left = index + 1
      var right = sorted.length - 1
      while (left < right) {
        val total = sorted(index) + sorted(left) + sorted(right)
        if (total < target) {
          count += right - left
          left += 1
        } else {
          right -= 1
        }
      }
      index += 1
    }
    count
  }
}
