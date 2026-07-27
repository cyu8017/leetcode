// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

object Solution {
  def minOperations(nums: Array[Int], x: Int): Int = {
    val total = nums.sum
    val target = total - x
    if (target < 0) return -1
    var best = -1
    var left = 0
    var cur = 0
    for (right <- nums.indices) {
      cur += nums(right)
      while (cur > target) {
        cur -= nums(left)
        left += 1
      }
      if (cur == target && right - left + 1 > best) best = right - left + 1
    }
    if (best < 0) -1 else nums.length - best
  }
}
