// LeetCode 1000 - Minimum Cost to Merge Stones
// https://leetcode.com/problems/minimum-cost-to-merge-stones/

object Solution {
  def mergeStones(stones: Array[Int], k: Int): Int = {
    val n = stones.length
    if ((n - 1) % (k - 1) != 0) return -1
    val prefix = Array.ofDim[Int](n + 1)
    for (i <- stones.indices) prefix(i + 1) = prefix(i) + stones(i)
    val dp = Array.fill(n, n)(0)
    for (length <- k to n) {
      for (i <- 0 to n - length) {
        val j = i + length - 1
        var best = Int.MaxValue
        var m = i
        while (m < j) {
          best = math.min(best, dp(i)(m) + dp(m + 1)(j))
          m += k - 1
        }
        dp(i)(j) = best
        if ((length - 1) % (k - 1) == 0) {
          dp(i)(j) += prefix(j + 1) - prefix(i)
        }
      }
    }
    dp(0)(n - 1)
  }
}
