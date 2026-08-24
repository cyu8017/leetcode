// LeetCode 2811 - Check if it is Possible to Split Array
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

object Solution {
  def canSplitArray(nums: List[Int], m: Int): Boolean = {
    val n = nums.length
    if (n <= 2) return true
    var i = 0
    while (i + 1 < n) {
      if (nums(i) + nums(i + 1) >= m) return true
      i += 1
    }
    false
  }
}
