// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

object Solution {
  def minCost(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val INF = 1000000000000000000L
    val dp = Array.fill(n + 1)(INF)
    dp(0) = 0
    var i = 0
    while (i < n) {
      val freq = scala.collection.mutable.Map.empty[Int, Int]
      var trimmed = 0
      var j = i
      while (j < n) {
        val c = freq.getOrElse(nums(j), 0) + 1
        freq(nums(j)) = c
        if (c == 2) trimmed += 2
        else if (c > 2) trimmed += 1
        val cost = dp(i) + k + trimmed
        if (cost < dp(j + 1)) dp(j + 1) = cost
        j += 1
      }
      i += 1
    }
    dp(n).toInt
  }
}
