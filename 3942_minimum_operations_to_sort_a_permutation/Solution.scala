// LeetCode 3942 - Minimum Operations to Sort a Permutation
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val n = nums.length
    var zero = 0
    var i = 0
    var found = false
    while (i < n && !found) {
      if (nums(i) == 0) {
        zero = i
        found = true
      }
      i += 1
    }
    var ans = Int.MaxValue
    if (check(nums, zero, 1)) {
      ans = math.min(ans, zero)
      ans = math.min(ans, n - zero + 2)
    }
    if (check(nums, zero, -1)) {
      ans = math.min(ans, zero + 2)
      ans = math.min(ans, n - zero)
    }
    if (ans == Int.MaxValue) -1 else ans
  }

  private def check(nums: Array[Int], zero: Int, step: Int): Boolean = {
    val n = nums.length
    var i = 1
    while (i < n) {
      val prev = ((zero + (i - 1) * step) % n + n) % n
      val curr = ((zero + i * step) % n + n) % n
      if (nums(prev) > nums(curr)) return false
      i += 1
    }
    true
  }
}
