// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

object Solution {
  def countFairPairs(nums: Array[Int], lower: Int, upper: Int): Long = {
    java.util.Arrays.sort(nums)
    count(nums, upper) - count(nums, lower - 1)
  }

  private def count(nums: Array[Int], x: Int): Long = {
    var ans = 0L
    var l = 0
    var r = nums.length - 1
    while (l < r) {
      if (nums(l).toLong + nums(r) <= x) {
        ans += r - l
        l += 1
      } else r -= 1
    }
    ans
  }
}
