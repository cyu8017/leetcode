// LeetCode 0891 - Sum of Subsequence Widths
// https://leetcode.com/problems/sum-of-subsequence-widths/

object Solution {
  def sumSubseqWidths(nums: Array[Int]): Int = {
    val MOD = 1000000007
    val arr = nums.sorted
    val n = arr.length
    val pow2 = Array.ofDim[Long](n)
    pow2(0) = 1
    var i = 1
    while (i < n) {
      pow2(i) = (pow2(i - 1) * 2) % MOD
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      ans = (ans + arr(i).toLong * (pow2(i) - pow2(n - 1 - i))) % MOD
      i += 1
    }
    ((ans + MOD) % MOD).toInt
  }
}
