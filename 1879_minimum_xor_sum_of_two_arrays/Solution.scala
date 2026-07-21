// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

object Solution {
  def minimumXORSum(nums1: Array[Int], nums2: Array[Int]): Int = {
    val n = nums1.length
    val dp = Array.fill(1 << n)(Int.MaxValue / 2)
    dp(0) = 0
    for (mask <- 0 until (1 << n)) {
      val i = Integer.bitCount(mask)
      if (i < n) {
        for (j <- 0 until n if (mask & (1 << j)) == 0) {
          val nextMask = mask | (1 << j)
          val cost = dp(mask) + (nums1(i) ^ nums2(j))
          if (cost < dp(nextMask)) dp(nextMask) = cost
        }
      }
    }
    dp((1 << n) - 1)
  }
}
