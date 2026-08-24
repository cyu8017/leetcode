// LeetCode 3830 - Longest Alternating Subarray After Removing At Most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

object Solution {
  def longestAlternating(nums: Array[Int]): Int = {
    val n = nums.length
    val l1 = Array.fill(n)(1)
    val l2 = Array.fill(n)(1)
    val r1 = Array.fill(n)(1)
    val r2 = Array.fill(n)(1)
    var ans = 0
    var i = 1
    while (i < n) {
      if (nums(i - 1) < nums(i)) l1(i) = l2(i - 1) + 1
      else if (nums(i - 1) > nums(i)) l2(i) = l1(i - 1) + 1
      ans = math.max(ans, math.max(l1(i), l2(i)))
      i += 1
    }
    i = n - 2
    while (i >= 0) {
      if (nums(i + 1) > nums(i)) r1(i) = r2(i + 1) + 1
      else if (nums(i + 1) < nums(i)) r2(i) = r1(i + 1) + 1
      i -= 1
    }
    i = 1
    while (i < n - 1) {
      if (nums(i - 1) < nums(i + 1)) ans = math.max(ans, l2(i - 1) + r2(i + 1))
      else if (nums(i - 1) > nums(i + 1)) ans = math.max(ans, l1(i - 1) + r1(i + 1))
      i += 1
    }
    ans
  }
}
