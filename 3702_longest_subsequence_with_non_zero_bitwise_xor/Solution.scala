// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

object Solution {
  def longestSubsequence(nums: Array[Int]): Int = {
    var xorv = 0
    var cnt0 = 0
    for (x <- nums) {
      xorv ^= x
      if (x == 0) cnt0 += 1
    }
    val n = nums.length
    if (xorv != 0) n
    else if (cnt0 == n) 0
    else n - 1
  }
}
