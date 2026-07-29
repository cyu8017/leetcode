// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

object Solution {
  def maxSumAfterPartitioning(arr: Array[Int], k: Int): Int = {
    val n = arr.length
    val dp = Array.fill(n + 1)(0)
    for (i <- 1 to n) {
      var best = 0
      for (size <- 1 to math.min(k, i)) {
        best = math.max(best, arr(i - size))
        dp(i) = math.max(dp(i), dp(i - size) + best * size)
      }
    }
    dp(n)
  }
}
