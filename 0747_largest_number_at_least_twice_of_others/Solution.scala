// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

object Solution {
  def dominantIndex(nums: Array[Int]): Int = {
    var first = -1
    var second = -1
    var index = -1
    var i = 0
    while (i < nums.length) {
      if (nums(i) > first) {
        second = first
        first = nums(i)
        index = i
      } else if (nums(i) > second) second = nums(i)
      i += 1
    }
    if (first >= 2 * second) index else -1
  }
}
