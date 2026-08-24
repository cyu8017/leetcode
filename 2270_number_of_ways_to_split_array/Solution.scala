// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

object Solution {
  def waysToSplitArray(nums: Array[Int]): Int = {
    var total = 0L
    for (v <- nums) total += v
    var left = 0L
    var ans = 0
    var i = 0
    while (i + 1 < nums.length) {
      left += nums(i)
      if (left >= total - left) ans += 1
      i += 1
    }
    ans
  }
}
