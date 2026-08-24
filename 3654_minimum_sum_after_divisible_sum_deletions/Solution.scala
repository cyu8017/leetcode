// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

object Solution {
  def minArraySum(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val prefix = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = (prefix(i) + nums(i)) % k
      i += 1
    }
    val inf = 1L << 62
    val dp = new Array[Long](n + 1)
    val best = Array.fill(k)(inf)
    best(0) = 0
    i = 1
    while (i <= n) {
      dp(i) = dp(i - 1) + nums(i - 1)
      if (best(prefix(i)) < dp(i)) dp(i) = best(prefix(i))
      if (dp(i) < best(prefix(i))) best(prefix(i)) = dp(i)
      i += 1
    }
    dp(n)
  }
}
