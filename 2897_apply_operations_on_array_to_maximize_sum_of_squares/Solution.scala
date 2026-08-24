// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

object Solution {
  def maxSum(nums: Array[Int], k: Int): Int = {
    val mod = 1000000007
    val cnt = Array.fill(32)(0)
    nums.foreach { v =>
      for (b <- 0 until 32 if (v & (1 << b)) != 0) cnt(b) += 1
    }
    var ans = 0
    for (_ <- 0 until k) {
      var cur = 0
      for (b <- 0 until 32 if cnt(b) > 0) {
        cur |= 1 << b
        cnt(b) -= 1
      }
      ans = ((ans + 1L * (cur % mod) * (cur % mod) % mod) % mod).toInt
    }
    ans
  }
}
