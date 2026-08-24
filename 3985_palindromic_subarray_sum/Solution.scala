// LeetCode 3985 - Palindromic Subarray Sum
// https://leetcode.com/problems/palindromic-subarray-sum/

object Solution {
  def maxPalindromicSubarraySum(nums: Array[Int]): Long = {
    val n = nums.length
    val prefix = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + nums(i)
      i += 1
    }
    val odd = new Array[Int](n)
    var left = 0
    var right = -1
    i = 0
    while (i < n) {
      var radius = 1
      if (i <= right) {
        val mirror = left + right - i
        radius = odd(mirror)
        if (right - i + 1 < radius) radius = right - i + 1
      }
      while (i - radius >= 0 && i + radius < n && nums(i - radius) == nums(i + radius)) radius += 1
      odd(i) = radius
      if (i + radius - 1 > right) {
        left = i - radius + 1
        right = i + radius - 1
      }
      i += 1
    }
    val even = new Array[Int](n)
    left = 0
    right = -1
    i = 0
    while (i < n) {
      var radius = 0
      if (i <= right) {
        val mirror = left + right - i + 1
        radius = even(mirror)
        if (right - i + 1 < radius) radius = right - i + 1
      }
      while (i - radius - 1 >= 0 && i + radius < n && nums(i - radius - 1) == nums(i + radius)) radius += 1
      even(i) = radius
      if (i + radius - 1 > right) {
        left = i - radius
        right = i + radius - 1
      }
      i += 1
    }
    var answer = 0L
    i = 0
    while (i < n) {
      var sum = prefix(i + odd(i)) - prefix(i - odd(i) + 1)
      if (sum > answer) answer = sum
      if (even(i) > 0) {
        sum = prefix(i + even(i)) - prefix(i - even(i))
        if (sum > answer) answer = sum
      }
      i += 1
    }
    answer
  }
}
