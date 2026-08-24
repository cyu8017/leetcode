// LeetCode 3836 - Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum_score_using_exactly_k_pairs/

object Solution {
  def maxScore(nums1: Array[Int], nums2: Array[Int], K: Int): Long = {
    val n = nums1.length
    val m = nums2.length
    val NEG = Long.MinValue / 4
    val f = Array.ofDim[Long](n + 1, m + 1, K + 1)
    var i = 0
    while (i <= n) {
      var j = 0
      while (j <= m) {
        java.util.Arrays.fill(f(i)(j), NEG)
        j += 1
      }
      i += 1
    }
    f(0)(0)(0) = 0
    i = 0
    while (i <= n) {
      var j = 0
      while (j <= m) {
        var k = 0
        while (k <= K) {
          if (i > 0) f(i)(j)(k) = math.max(f(i)(j)(k), f(i - 1)(j)(k))
          if (j > 0) f(i)(j)(k) = math.max(f(i)(j)(k), f(i)(j - 1)(k))
          if (i > 0 && j > 0 && k > 0) {
            f(i)(j)(k) = math.max(f(i)(j)(k), f(i - 1)(j - 1)(k - 1) + nums1(i - 1).toLong * nums2(j - 1))
          }
          k += 1
        }
        j += 1
      }
      i += 1
    }
    f(n)(m)(K)
  }
}
