// LeetCode 3857 - Minimum Cost To Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

object Solution {
  def minCost(n: Int): Int = n * (n - 1) / 2
}
