// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

object Solution {
  def sumIndicesWithKSetBits(nums: Array[Int], k: Int): Int = {
    var ans = 0
    for (i <- nums.indices) if (Integer.bitCount(i) == k) ans += nums(i)
    ans
  }
}
