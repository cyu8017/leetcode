// LeetCode 1799 - Maximize Score After N Operations
// https://leetcode.com/problems/maximize-score-after-n-operations/

object Solution {
  def maxScore(nums: Array[Int]): Int = {
    val n = nums.length
    val memo = Array.fill(1 << n)(-1)

    def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)

    def dp(mask: Int): Int = {
      if (mask == (1 << n) - 1) return 0
      if (memo(mask) != -1) return memo(mask)
      val step = Integer.bitCount(mask) / 2 + 1
      var best = 0
      for (i <- 0 until n if (mask >> i & 1) == 0) {
        for (j <- i + 1 until n if (mask >> j & 1) == 0) {
          best = math.max(
            best,
            step * gcd(nums(i), nums(j)) + dp(mask | (1 << i) | (1 << j))
          )
        }
      }
      memo(mask) = best
      best
    }

    dp(0)
  }
}
