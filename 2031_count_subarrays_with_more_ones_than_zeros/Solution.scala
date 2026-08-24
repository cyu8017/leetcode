// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

object Solution {
  def subarraysWithMoreZerosThanOnes(nums: Array[Int]): Int = {
    val MOD = 1000000007
    val n = nums.length
    val offset = n + 1
    val bit = Array.ofDim[Int](2 * n + 7)
    def add(i0: Int, v: Int): Unit = {
      var i = i0
      while (i < bit.length) { bit(i) += v; i += i & -i }
    }
    def sum(i0: Int): Int = {
      var i = i0
      var s = 0
      while (i > 0) { s += bit(i); i -= i & -i }
      s
    }
    var pref = 0
    var ans = 0
    add(offset, 1)
    nums.foreach { x =>
      pref += (if (x == 1) 1 else -1)
      val idx = pref + offset
      ans = (ans + sum(idx - 1)) % MOD
      add(idx, 1)
    }
    ans
  }
}
