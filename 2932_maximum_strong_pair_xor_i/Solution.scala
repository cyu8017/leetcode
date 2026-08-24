// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

object Solution {
  def maximumStrongPairXor(nums: Array[Int]): Int = {
    var ans = 0
    for (i <- nums.indices; j <- i until nums.length) {
      val x = nums(i)
      val y = nums(j)
      if (math.abs(x - y) <= math.min(x, y)) {
        val xorr = x ^ y
        if (xorr > ans) ans = xorr
      }
    }
    ans
  }
}
