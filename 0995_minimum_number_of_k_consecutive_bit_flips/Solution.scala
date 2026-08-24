// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

object Solution {
  def minKBitFlips(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val flip = Array.ofDim[Int](n)
    var ans = 0
    var flipped = 0
    var i = 0
    while (i < n) {
      if (i >= k) flipped ^= flip(i - k)
      if (nums(i) == flipped) {
        if (i + k > n) return -1
        ans += 1
        flipped ^= 1
        flip(i) = 1
      }
      i += 1
    }
    ans
  }
}
