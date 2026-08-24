// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

object Solution {
  def maximumTotalCost(nums: Array[Int]): Long = {
    val NEG = -1000000000000000000L
    val n = nums.length
    val memo = Array.fill(n, 2)(NEG)
    def dfs(i: Int, j: Int): Long = {
      if (i >= n) return 0L
      if (memo(i)(j) != NEG) return memo(i)(j)
      var res = nums(i).toLong + dfs(i + 1, 1)
      if (j > 0) res = math.max(res, -nums(i).toLong + dfs(i + 1, 0))
      memo(i)(j) = res
      res
    }
    dfs(0, 0)
  }
}
