// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

object Solution {
  def largestSumOfAverages(nums: Array[Int], k: Int): Double = {
    val n = nums.length
    val prefix = Array.ofDim[Double](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + nums(i)
      i += 1
    }
    var dp = Array.tabulate(n)(i => (prefix(i + 1) - prefix(0)) / (i + 1))
    var groups = 2
    while (groups <= k) {
      val nxt = Array.ofDim[Double](n)
      i = groups - 1
      while (i < n) {
        var best = 0.0
        var j = groups - 2
        while (j < i) {
          best = math.max(best, dp(j) + (prefix(i + 1) - prefix(j + 1)) / (i - j))
          j += 1
        }
        nxt(i) = best
        i += 1
      }
      dp = nxt
      groups += 1
    }
    dp(n - 1)
  }
}
