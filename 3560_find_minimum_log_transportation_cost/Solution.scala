// LeetCode 3560 - Find Minimum Log Transportation Cost
// https://leetcode.com/problems/find-minimum-log-transportation-cost/

object Solution {
  def minCuttingCost(n: Int, m: Int, k: Int): Long = {
    val x = math.max(n, m)
    if (x <= k) 0L else 1L * k * (x - k)
  }
}
