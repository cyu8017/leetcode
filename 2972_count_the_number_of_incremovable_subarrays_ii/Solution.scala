// LeetCode 2972 - Count the Number of Incremovable Subarrays II
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/

object Solution {
  def incremovableSubarrayCount(nums: Array[Int]): Long = {
    val n = nums.length
    var left = 0
    while (left + 1 < n && nums(left) < nums(left + 1)) left += 1
    if (left == n - 1) return n.toLong * (n + 1) / 2
    var ans = left + 2L
    var right = n - 1
    while (right > 0 && (right == n - 1 || nums(right) < nums(right + 1))) {
      while (left >= 0 && nums(left) >= nums(right)) left -= 1
      ans += left + 2
      right -= 1
      if (right > 0 && nums(right) >= nums(right + 1)) return ans
    }
    ans
  }
}
