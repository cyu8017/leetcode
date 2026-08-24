// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

object Solution {
  def maximumStrongPairXor(nums: Array[Int]): Int = {
    val a = nums.sorted
    var ans = 0
    for (i <- a.indices) {
      val x = a(i)
      var j = i
      while (j < a.length && a(j) <= 2 * x) {
        val xorr = x ^ a(j)
        if (xorr > ans) ans = xorr
        j += 1
      }
    }
    ans
  }
}
