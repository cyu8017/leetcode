// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

object Solution {
  def maximumJumps(nums: Array[Int], target: Int): Int = {
    val n = nums.length
    val dp = Array.fill(n)(-1)
    dp(0) = 0
    var i = 0
    while (i < n) {
      if (dp(i) >= 0) {
        var j = i + 1
        while (j < n) {
          if (math.abs(nums(j) - nums(i)) <= target) dp(j) = math.max(dp(j), dp(i) + 1)
          j += 1
        }
      }
      i += 1
    }
    dp(n - 1)
  }
}
